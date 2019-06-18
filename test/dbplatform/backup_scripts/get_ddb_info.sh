#!/bin/bash
#set -e

software_path={0}
ip={1}
role={2}


#test directory exists
if [  -d ${software_path} ];then
if [ ${role} == "QS" ];then
#modify qs url
cd ${software_path}/conf
ddb_name=`grep '<ddb_name>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e ddb_name:${ddb_name}
name=`grep '<name>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e name:${name}
url=`grep '<url>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e url:${url}
port=`grep '<port>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e port:${port}

else
cd ${software_path}/conf
name=`grep '<name>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e name:${name}
ip=`grep '<ip>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e ip:${ip}
port=`grep '<port>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e port:${port}
sysdb_url=`grep '<sysdb_url>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e sysdb_url:${sysdb_url}
sysdb_user=`grep '<sysdb_user>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e sysdb_user:${sysdb_user}
sysdb_password=`grep '<sysdb_password>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
echo -e sysdb_password:${sysdb_password}
echo -e ${role}

fi
else
echo -e  "ddb software_path is" ${software_path} "not exists"
exit 1
fi

if  [ $? -eq 0 ]; then
echo "success get ddb info  on ip:${ip},path:${software_path},role:${role}"
fi