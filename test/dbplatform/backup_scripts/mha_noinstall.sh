#!/bin/bash
#set -e
# Parameter interpretation
# vip               virtual IP
# netWork           Network card name
# instance_num      the number of instance
# cluser_name       cluster name
# instance_info     the information of instance(include ip,port)
# install_type	    The type of setup,include master,slave,manager
# sys_name          system name

vip={0}
netWork={1}
instance_num={2}
cluser_name={3}
instance_info={4}
install_type={5}
sys_name={6}

setup_path=/opt/mha/$sys_name/$cluser_name

# Checking the directory exists
echo "Check the installation package and the installation path:/tmp/mha_install.tar.gz and /opt"
if [[ -d /opt && -f /tmp/mha_install.tar.gz ]];then
    echo "Installation package and installation path check OK"
else
    echo "Installation package or installation path is not exist,Failed to install"
    install_status=false
    exit 1
fi

# Installation according to installation type
if [[ $install_type == 'master' ]];then
    echo "master is Installed,not need to install"

    # install package
	echo "Install the node as master, unzip package."
	tar -zxvf /tmp/mha_install.tar.gz -C /tmp/
	if [[ $? -eq 0 ]];then
		echo "Unzip success,install the node package"
	else
		echo "Unzip failed"
		install_status=false
		exit 1
	fi

    echo "Check whether the correct netWork"
    net_status=`/usr/sbin/ifconfig | grep $netWork | wc -l`
    if [[ $net_status -ge 1 ]];then
        echo "$netWork is exists, generates VIP script and mounts VIP"
    else
        echo "$netWork is not exists,Failed to install"
        exit 1
    fi

	# generates VIP script and mounts VIP
	sed -i "/VIP=/c VIP=$vip" /tmp/mha/vip.sh
	cp /tmp/mha/vip.sh /home/mhamonitor/
	g_vip="$vip""/24"
	/sbin/ip addr add $g_vip dev $netWork
	vip_status=`ip a | grep $vip | wc -l`
	if [[ $vip_status -ge 1 ]];then
		echo "mounts VIP success"
	else
		echo "mounts VIP failed,Failed to install"
		install_status=false
		exit 1
	fi

	echo "Check whether mhamonitor users exist"
    id -u mhamonitor
    if [[ $? -ne 0 && -f /home/mhamonitor/.ssh/id_rsa.pub ]];then
        echo "mhamonitor users and key is exist,get secret key"
        key=`cat /home/mhamonitor/.ssh/id_rsa.pub`
        echo -n "mha_begin:$key""mha_end"
    else
        echo "mhamonitor users or key is not exist,cmdb information is error"
        exit 1
    fi
elif [[ $install_type == 'slave' ]];then
    echo "slave is Installed,not need to install"

    # install package
	echo "Install the node as master, unzip package."
	tar -zxvf /tmp/mha_install.tar.gz -C /tmp/
	if [[ $? -eq 0 ]];then
		echo "Unzip success,install the node package"
	else
		echo "Unzip failed"
		install_status=false
		exit 1
	fi

    echo "Check whether the correct netWork"
    net_status=`/usr/sbin/ifconfig | grep $netWork | wc -l`
    if [[ $net_status -ge 1 ]];then
        echo "$netWork is exists, generates VIP script and mounts VIP"
    else
        echo "$netWork is not exists,Failed to install"
        exit 1
    fi

	# generates VIP script and mounts VIP
	sed -i "/VIP=/c VIP=$vip" /tmp/mha/vip.sh
	cp /tmp/mha/vip.sh /home/mhamonitor/

	echo "Check whether mhamonitor users exist"
    id -u mhamonitor
    if [[ $? -ne 0 && -f /home/mhamonitor/.ssh/id_rsa.pub ]];then
        echo "mhamonitor users and key is exist,get secret key"
        key=`cat /home/mhamonitor/.ssh/id_rsa.pub`
        echo -n "mha_begin:$key""mha_end"
    else
        echo "mhamonitor users or key is not exist,cmdb information is error"
        exit 1
    fi
eif [[ $install_type == 'manager' ]];then
    # install package
	echo "Install the node as manager, unzip package."
	tar -zxvf /tmp/mha_install.tar.gz -C /tmp/
	if [[ $? -eq 0 ]];then
		echo "Unzip success,install the node and manager package"
    else
		echo "Unzip failed"
		install_status=false
		exit 1
	fi

	echo "Check whether mhamonitor users exist"
    id -u mhamonitor
    if [[ $? -ne 0 && -f /home/mhamonitor/.ssh/id_rsa.pub ]];then
        echo "mhamonitor users and key is exist,get secret key"
        key=`cat /home/mhamonitor/.ssh/id_rsa.pub`
        echo -n "mha_begin:$key""mha_end"
    else
        echo "mhamonitor users or key is not exist,cmdb information is error"
        exit 1
    fi

	# Generate configuration files
	echo "create the directory of configuration files"
	mkdir -pv $setup_path/conf
	conf_dir=`echo $?`
	mkdir -pv $setup_path/log
	log_dir=`echo $?`
	mkdir -pv $setup_path/manage
	manage_dir=`echo $?`
	if [[ $conf_dir -eq 0 && $log_dir -eq 0 && $manage_dir -eq 0 ]];then
		echo "create directory success,Generate configuration files"
		gateway=`echo $vip | awk -F"." '{print $1}'`"."`echo $vip | awk -F"." '{print $2}'`"."`echo $vip | awk -F"." '{print $3}'`".254"

		sed -i "s/Virtual_IP/$vip/g" /tmp/mha/master_ip_failover
		sed -i "s/Gateway_IP/$gateway/g" /tmp/mha/master_ip_failover
		sed -i "s/netWork/$netWork/g" /tmp/mha/master_ip_failover
		sed -i "s/Virtual_IP/$vip/g" /tmp/mha/master_ip_online_change
		sed -i "s/Gateway_IP/$gateway/g" /tmp/mha/master_ip_online_change
		sed -i "s/netWork/$netWork/g" /tmp/mha/master_ip_online_change

		# mha.conf
		echo "[server default]" >> $setup_path/conf/mha.conf
        echo "manager_workdir=$setup_path/log/" >> $setup_path/conf/mha.conf
        echo "manager_log=$setup_path/log/manager.log" >> $setup_path/conf/mha.conf
        echo "ssh_user=mhamonitor" >> $setup_path/conf/mha.conf
        echo "ssh_port=14816" >> $setup_path/conf/mha.conf
        echo "repl_user=repl" >> $setup_path/conf/mha.conf
        echo "repl_password=111111" >> $setup_path/conf/mha.conf
        echo "ping_interval=3" >> $setup_path/conf/mha.conf
        echo "master_ip_failover_script=/opt/mha/$sys_name/$cluser_name/conf/master_ip_failover" >> $setup_path/conf/mha.conf
        echo "master_ip_online_change_script=/opt/mha/$sys_name/$cluser_name/conf/master_ip_online_change" >> $setup_path/conf/mha.conf

		for((i=1;i<=$instance_num;i++))
		do
			info=`echo $instance_info | cut -d"," -f$i`
			ip_info=`echo $info | cut -d"_" -f1`
			port_info=`echo $info | cut -d"_" -f2`
			echo "[server$i]" >> $setup_path/conf/mha.conf
			echo "hostname=$ip_info" >> $setup_path/conf/mha.conf
			echo "user=bkagent" >> $setup_path/conf/mha.conf
			echo "password=111111" >> $setup_path/conf/mha.conf
			echo "port=$port_info" >> $setup_path/conf/mha.conf
			echo "master_binlog_dir=/opt/mysql$port_info/log" >> $setup_path/conf/mha.conf
			echo "check_repl_delay=0" >> $setup_path/conf/mha.conf
			echo "candidate_master=1" >> $setup_path/conf/mha.conf
		done
		cp /tmp/mha/master_ip_failover $setup_path/conf
		cp /tmp/mha/master_ip_online_change $setup_path/conf
		chown -R mhamonitor.mhamonitor /opt/mha
	else
		echo "create directory failed"
		install_status=false
		exit 1
	fi
else
    echo "Incorrect installation type,Failed to install"
    install_status=false
    exit 1
fi
