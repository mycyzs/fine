#!/bin/bash
#set -e

function check_os_env(){
if [ "$(sudo chkconfig --list|grep iptables)" != "iptables       	0:off	1:off	2:off	3:off	4:off	5:off	6:off" ] || [ "$(sudo service iptables status|cut -d: -f2)" != " Firewall is not running." ];then
	sudo service iptables stop
	sudo chkconfig iptables off
	sudo service iptables status
	sudo chkconfig --list|grep iptables
fi

if [ "$(sudo getenforce)" != "Disabled" ] || [ "$(sudo cat /etc/selinux/config|grep -w "^SELINUX"|awk -F"=" '{print $2}')" != "disabled" ];then
	sudo /bin/cp /etc/selinux/config /tmp/config; sudo setenforce 0; sudo sed -i "/^SELINUX=/c SELINUX=disabled" /etc/selinux/config
	sudo getenforce; sudo cat /etc/selinux/config|grep -w "^SELINUX"
fi

if [ "$(sudo cat /proc/sys/vm/swappiness)" != "1" ] || [ "$(sudo cat /etc/sysctl.conf|grep vm.swappiness|awk -F"=" '{print $2}')" != "1" ];then
	sudo /bin/cp /etc/sysctl.conf /tmp/sysctl.conf; sudo sysctl vm.swappiness=1
	if [ -z "$(sudo cat /etc/sysctl.conf|grep -w "^vm.swappiness")" ];then
		sudo  sh -c 'echo "vm.swappiness = 1" >> /etc/sysctl.conf'
	else
		sudo sed -i "/vm.swappiness/c vm.swappiness=1" /etc/sysctl.conf
	fi
	sudo cat /etc/sysctl.conf|grep -w "vm.swappiness"
fi

if [ "$(sudo cat /proc/sys/kernel/sem)" != "250	32000	100	128" ] || [ "$(sudo cat /etc/sysctl.conf|grep kernel.sem|awk -F"=" '{print $2}')" != "250 32000 100 128" ];then
	sudo /bin/cp /etc/sysctl.conf /tmp/sysctl.conf; sudo sysctl kernel.sem="250 32000 100 128"
	if [ -z "$(sudo cat /etc/sysctl.conf|grep -w ^kernel.sem)" ];then
		sudo sh -c 'echo "kernel.sem = 250 32000 100 128" >> /etc/sysctl.conf'
	else
		sudo sed -i "/kernel.sem/c kernel.sem = 250 32000 100 128" /etc/sysctl.conf
	fi
	sudo cat /etc/sysctl.conf|grep -w "kernel.sem"
fi

if [ "$(sudo cat /sys/kernel/mm/redhat_transparent_hugepage/enabled|awk -F" " '{print $2}')" != "[never]" ] || [ -z "$(sudo grep 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' /etc/rc.local)" ] || [ -z "$(sudo grep 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' /etc/rc.local)" ];then
	sudo /bin/cp /etc/rc.local /tmp/rc.local; sudo sh -c 'echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled'
	sudo sh -c 'echo -e "if test -f /sys/kernel/mm/transparent_hugepage/enabled; then\necho never > /sys/kernel/mm/transparent_hugepage/enabled\nfi\n" >> /etc/rc.local; sudo echo -e "if test -f /sys/kernel/mm/transparent_hugepage/defrag; then\necho never > /sys/kernel/mm/transparent_hugepage/defrag\nfi\n" >> /etc/rc.local'
	sudo cat /sys/kernel/mm/redhat_transparent_hugepage/enabled; sudo cat /etc/rc.local
fi

if [ ! -f "/etc/security/limits.d/90-nofile.conf" ] || [ -z "$(sudo cat /etc/security/limits.d/90-nofile.conf|grep 1048576)" ];then
	sudo sh -c 'echo -e "# PLAYBOOK VERSION: 1610 \n \n*  soft  nofile  1048576\n*  hard  nofile  1048576\n" > /etc/security/limits.d/90-nofile.conf'
fi

if [ -z "$(sudo grep 'transparent_hugepage=never' /etc/grub.conf)" ];then
	sudo /bin/cp /etc/grub.conf /tmp/grub.conf; sudo sed -i '/vmlinuz-'$(uname -r)'/s/$/ transparent_hugepage=never/' /etc/grub.conf
	sudo cat /etc/grub.conf
fi
if [ -z "$(sudo grep 'numa=off' /etc/grub.conf)" ];then
	sudo /bin/cp /etc/grub.conf /tmp/grub.conf; sudo sed -i '/vmlinuz-'$(uname -r)'/s/$/ numa=off/' /etc/grub.conf
	sudo cat /etc/grub.conf
fi
if [ -z "$(sudo grep 'elevator=deadline' /etc/grub.conf)" ];then
	sudo /bin/cp /etc/grub.conf /tmp/grub.conf; sudo sed -i '/vmlinuz-'$(uname -r)'/s/$/ elevator=deadline/' /etc/grub.conf
	sudo cat /etc/grub.conf
fi
}

#Check mysql env.
function check_mysql_env(){
sudo_root=`sudo -A -l 2> /dev/null`
if [[ $? -eq 0 ]];then
	echo "access,go on"
else
	echo "you can't sudo to root"
	exit 0
fi

sudo yum list all > /dev/null
if [[ $? -eq 0 ]];then
	echo "yum source have no problem"
else
	echo "yum source have error"
	exit 0
fi

sudo yum install -y perl-Time-HiRes make gcc-c++ bison ncurses-devel libaio libaio-devel time numactl-devel gperftools-devel
yum_num=`sudo yum list installed | grep -E "^perl-Time-HiRes.x86_64|^make.x86_64|^gcc-c\+\+.x86_64|^bison.x86_64|^ncurses-devel.x86_64|^libaio.x86_64|^libaio-devel.x86_64|^time.x86_64|numactl-devel.x86_64|^gperftools-devel.x86_64" |wc -l`
if [[ $yum_num -eq 10 ]];then
	echo "Dependency package may be installed successfully,continue install"
else
	echo "Dependency package may be installed faild"
	exit 0
fi

if [ $(sudo netstat -tunlp | grep -w $port|wc -l) = "0" ];then
	echo "mysql$port process no exist,continue the installation"
else
	echo "mysql$port process is exist,abort the installation"
	exit 0
fi

if [ -d "/opt/mysql$port" ];then
	echo "The datadir of mysql$port exists,abort the install"
	exit 0
else
	echo "The datadir of mysql$port no exists,continue the install"
fi
}

#install mysql
function install_mysql(){
#check user and environment variables.
sudo id -u mysql >/dev/null 2>&1
if [[ $? -eq 0 ]];then
	echo "mysql user exists,continue"
	sudo sh -c 'echo -e "[client]\nuser=root\npassword=RootPasInlt\n[mysql]\ndefault-character-set = utf8\nmax_allowed_packet = 1G\nno-auto-rehash" > /home/mysql/.my.cnf'
	sudo sh -c "echo 'prompt = [\\u@\\h][\\d][\\r:\\m:\\s]>\\_' >> /home/mysql/.my.cnf"
	sudo chown -R mysql.mysql /home/mysql/.my.cnf
else
	sudo groupadd mysql  && sudo useradd -g mysql mysql  && sudo chage -M -1 mysql && sudo passwd -l mysql
	sudo sh -c 'echo -e "[client]\nuser=root\npassword=RootPasInlt\n[mysql]\ndefault-character-set = utf8\nmax_allowed_packet = 1G\nno-auto-rehash" > /home/mysql/.my.cnf'
	sudo sh -c "echo 'prompt = [\\u@\\h][\\d][\\r:\\m:\\s]>\\_' >> /home/mysql/.my.cnf"
	sudo chown -R mysql.mysql /home/mysql/.my.cnf
fi

mysqltar=`sudo echo $version | awk -F"/" '{print $NF}' | awk -F".tar" '{print $1}'`
if [ ! -d "/usr/local/$mysqltar" ];then
	sudo tar -xvf /tmp/$version -C /usr/local/
	if [[ $? -eq 0 ]];then
		echo "uncompress success"
	else
		echo "Uncompress failed"
		exit 0
	fi
else
	echo "no Uncompress,continue"
fi

if [ $(ls -l $default_basedir | awk '{print $9}' | grep "mysql$" | wc -l) = "0" ];then
	sudo ln -s /usr/local/$mysqltar /usr/local/mysql
	if [[ $? -eq 0 ]];then
		echo "do link success"
	else
		echo "do link failed"
		exit 0
	fi
fi

sudo sh -c "echo 'export PATH=/usr/local/mysql/bin:$PATH' >> /etc/profile" && source /etc/profile

sudo mkdir -pv /opt/mysql$port/{log,data,tmp}
sudo chown -R mysql.mysql /opt/mysql$port
sudo mv /tmp/my$port.cnf /opt/mysql$port/my.cnf
if [[ $? -eq 0 ]];then
	echo "/tmp/my$port.cnf exists,continue"
else
	echo "/tmp/my$port.cnf no exist,abort"
	exit 0
fi

sudo $default_basedir/mysql/bin/mysqld --defaults-file=/opt/mysql$port/my.cnf --user=mysql  --datadir=/opt/mysql$port/data --initialize
if [[ $? -eq 0 ]];then
	echo "initialize successfully"
else
	echo "initialize failed"
	exit 0
fi

sudo chmod 644 /opt/mysql$port/my.cnf
sudo chown -R mysql.mysql /opt/mysql$port/my.cnf

sudo /bin/cp $default_basedir/mysql/support-files/mysql.server /etc/init.d/mysqld$port
sudo sed -i 's/^basedir=/basedir=\/usr\/local\/mysql/g' /etc/init.d/mysqld$port
sudo sed -i "/^basedir=\/usr\/local\/mysql/a\mysql_dir=\/opt\/mysql$port" /etc/init.d/mysqld$port
sudo sed -i 's/^datadir=/datadir=$mysql_dir\/data/g' /etc/init.d/mysqld$port
sudo sed -i 's/^mysqld_pid_file_path=/mysqld_pid_file_path=$datadir\/pid/g' /etc/init.d/mysqld$port
sudo sed -i '/extra_args=\"-e $basedir\/my.cnf\"/a\else extra_args=\"-e $mysql_dir\/my.cnf\"' /etc/init.d/mysqld$port
sudo sed -i '/$bindir\/mysqld_safe --datadir="$datadir" --pid-file="$mysqld_pid_file_path"/c $bindir\/mysqld_safe --defaults-file="$mysql_dir/my.cnf" --pid-file="$mysqld_pid_file_path" $other_args >\/dev\/null &' /etc/init.d/mysqld$port


sudo chown -R mysql.mysql /etc/init.d/mysqld$port
sudo chown -R mysql.mysql $default_basedir/mysql
sudo chown -R mysql.mysql $default_basedir/$mysqltar

sudo su - mysql << EOF
source /etc/profile
service mysqld$port start
EOF

sleep 10
if [ -n $(sudo netstat -tunlp | grep -w $port | awk -F::: '{print $2}') ];then
	echo "mysqld$port start sucessful!"
else
	echo "mysqld$port start failed!"
	exit 0
fi

PASSWORD=`sudo cat /opt/mysql$port/data/error.log | grep "A temporary password is generated for root@localhost" | sed 's/^.*root@localhost: //g'`
mysqladmin -u root -p"$PASSWORD" password RootPasInlt -S /opt/mysql$port/data/mysql.sock
mysql -uroot -pRootPasInlt -S /opt/mysql$port/data/mysql.sock  -e "set session sql_log_bin=0;create user 'repl'@'%' identified by '111111';grant replication slave,replication client on *.* to 'repl'@'%';create user 'bkagent'@'%' identified by '111111';grant all on *.* to 'bkagent'@'%' with grant option;create user 'mha'@'%' identified by 'mhaPass';grant all on *.* to 'mha'@'%';create user 'agent'@'127.0.0.1' identified by 'agent_password';grant select, replication client,show databases,process on *.* to 'agent'@'127.0.0.1';set session sql_log_bin=1;reset master;\q"
if [[ $? -eq 0 ]];then
	echo "modify password successfully"
	echo "success install mysqld$port."
else
	echo "modify password failed"
	echo "failed install mysqld$port."
	exit 0
fi
}

# The execution body of the script.
if [[ $# -eq "0" ]];then
  default_basedir="/usr/local"
  version={1}
  port={0}

  echo "{mysqlParameter}">/tmp/my${port}.cnf
  check_mysql_env $port
  check_os_env
  install_mysql $version $port
else
  echo "tar file and my.cnf are /tmp,Please enter the correct options.for example:cd /tmp;$0 mysql-5.7.16-linux-glibc2.5-x86_64.tar.gz 3306"
  exit 0
fi