#!/bin/bash
#set -e

software_path={0}
ip={1}
role={2}
ddb_name={3}
name={4}
master_url={5}

master_name={6}
master_ip={7}
sysdb_port={sysdb_ip_port}
sysdb_name={sysdb_name}
sysdb_user={9}
sysdb_password={10}

sysdb_url=jdbc:mysql:\/\/{sysdb_ip_port}\/{sysdb_name}

echo ${sysdb_url}

if [ ${role} == "QS" ];then
#modify qs url
cd ${software_path}/conf
sed -i 's/<name>.*<\/name>/<name>'${name}'<\/name>/g'  ${software_path}/conf/QSServerConf.xml
sed -i 's/<ddb_name>.*<\/ddb_name>/<ddb_name>'${name}'<\/ddb_name>/g'  ${software_path}/conf/QSServerConf.xml
sed -i 's/<url>.*<\/url>/<url>'${master_url}'<\/url>/g'  ${software_path}/conf/QSServerConf.xml

after_ddb_name=`grep '<ddb_name>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_name=`grep '<name>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_url=`grep '<url>' QSServerConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`

if [ ${after_ddb_name} == ${ddb_name} -a  ${after_ddb_name} == ${ddb_name} -a ${after_ddb_name} == ${ddb_name} ];then
echo -e "success modify ddb info  on ip:${ip},path:${software_path},role:${role}"
else
echo -e "fail modify ddb info  on ip:${ip},path:${software_path},role:${role}"
fi

else
cd ${software_path}/conf

sed -i 's/<name>.*<\/name>/<name>'${master_name}'<\/name>/g'  ${software_path}/conf/DBClusterConf.xml
sed -i 's/<ip>.*<\/ip>/<ip>'${master_ip}'<\/ip>/g'  ${software_path}/conf/DBClusterConf.xml
sed -i 's/<sysdb_url>.*<\/sysdb_url>/<sysdb_url>jdbc:mysql:\/\/{sysdb_ip_port}\/{sysdb_name}<\/sysdb_url>/g'  ${software_path}/conf/DBClusterConf.xml
sed -i 's/<sysdb_user>.*<\/sysdb_user>/<sysdb_user>'${sysdb_user}'<\/sysdb_user>/g'  ${software_path}/conf/DBClusterConf.xml
sed -i 's/<sysdb_password>.*<\/sysdb_password>/<sysdb_password>'${sysdb_password}'<\/sysdb_password>/g'  ${software_path}/conf/DBClusterConf.xml

after_name=`grep '<name>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_ip=`grep '<ip>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_sysdb_url=`grep '<sysdb_url>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_sysdb_user=`grep '<sysdb_user>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`
after_sysdb_password=`grep '<sysdb_password>' DBClusterConf.xml |awk -F '>' '{print $2}' |awk -F '<' '{print $1}'`

if [ ${master_name} == ${after_name} -a  ${master_ip} == ${after_ip} -a "${sysdb_url}" == "${after_sysdb_url}" -a  ${sysdb_user} == ${after_sysdb_user} -a ${sysdb_password} == ${after_sysdb_password} ];then
echo -e "success modify ddb info  on ip:${ip},path:${software_path},role:${role}"
echo -e "success"
else
echo -e "fail modify ddb info  on ip:${ip},path:${software_path},role:${role}"
echo -e "fail"
fi

fi


