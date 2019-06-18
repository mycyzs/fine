#!/bin/bash
#set -e
ddb_packages={1}
software_path={0}
master_url={4}
name={5}
ip={2}
port={3}
role={6}
java_packages={7}
uncompress_java_file={8}

#check user and environment variables.
id -u qs >/dev/null 2>&1
if [ $? -eq 0 ];then
	echo "qs user exists,continue"
	if [ ! -d /opt/ddb/ ];then
    mkdir -p /opt/ddb
    chown -R qs:qs /opt/ddb
    fi
    if [ ! -d  ${software_path} ];then
        echo -e "ddb path not exists"
        mkdir -p ${software_path}
        tar  xvf /tmp/${ddb_packages}  -C ${software_path}
        chown -R qs:qs ${software_path}
        if [ $? -eq 0 ];then
            echo "uncompress ddb software on ip:${ip},port:${port}"
        fi
     else
     echo "ddb path exists"
     exit 0
     fi

    if [ ! -d /usr/local/${uncompress_java_file} ];then
    echo "java software not exists"
    tar xvf /tmp/${java_packages} -C /usr/local/
    chown -R qs:qs /usr/local/${uncompress_java_file}
    fi
    #configure qs user env
    echo "JAVA_HOME=/usr/local/${uncompress_java_file}" >>/home/qs/.bash_profile
    echo "PATH=\${JAVA_HOME}/bin:\$PATH" >>/home/qs/.bash_profile
    echo "export PATH">>/home/qs/.bash_profile

else
echo "qs not exists"
groupadd qs  && useradd -g qs qs  && chage -M -1 qs && passwd -l qs
if [ ! -d /opt/ddb/ ];then
mkdir -p /opt/ddb
chown -R qs:qs /opt/ddb
fi
    if [ ! -d  ${software_path} ];then
        echo -e "ddb path not exists"
        mkdir -p ${software_path}
        tar  xvf /tmp/${ddb_packages}  -C ${software_path}
        chown -R qs:qs ${software_path}
        if [ $? -eq 0 ];then
            echo "uncompress ddb software on ip:${ip},port:${port}"
        fi
     else
     echo "ddb path exists"
     exit 0
     fi

    check_java=`ls -ld  /usr/local/${uncompress_java_file}`
    if [ -z ${check_java} ];then
    echo "java software not exists"
    tar xvf /tmp/${java_packages} -C /usr/local
    chown -R qs:qs /usr/local/${uncompress_java_file}
    fi
    #configure qs user env
    check_java_env=`more /home/qs/.bash_profile |grep JAVA_HOME=/usr/local/${uncompress_java_file}`
    if [ -z ${check_java_env} ];then
    echo "JAVA_HOME=/usr/local/${uncompress_java_file}" >>/home/qs/.bash_profile
    echo "PATH=\${JAVA_HOME}/bin:\$PATH" >>/home/qs/.bash_profile
    echo "export PATH">>/home/qs/.bash_profile
    fi
fi

if [ ${role} == "QS" ];then
#modify qs url
sed -i 's/<port>.*<\/port>/<port>'${port}'<\/port>/g'  ${software_path}/conf/QSServerConf.xml
sed -i 's/<name>.*<\/name>/<name>'${name}'<\/name>/g'  ${software_path}/conf/QSServerConf.xml
sed -i 's/<ddb_name>.*<\/ddb_name>/<ddb_name>'${name}'<\/ddb_name>/g'  ${software_path}/conf/QSServerConf.xml
sed -i 's/<url>.*<\/url>/<url>'${master_url}'<\/url>/g'  ${software_path}/conf/QSServerConf.xml
fi




if  [ $? -eq 0 ]; then
echo "success install qs on ip:${ip},port:${port}"
fi