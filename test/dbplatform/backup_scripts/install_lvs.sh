#!/bin/bash
#set -e
ip=${ip}
lastoneip=`echo ${ip} |cut -d \. -f 4`
lvs_role={lvs_role}
lvs_network={lvs_network}
lvs_vip={lvs_vip}
lvs_port={lvs_port}
qsiplist={qsiplist}
if [ {lvs_role} == 'MASTER' ];then
lvs_priority=100
else
lvs_priority=90
fi



cd /tmp
tar xvf Lvs-Keepalived.tar && cd  Lvs-Keepalived

if [ $? -eq 0 ] ;then
echo "success uncompress   kp+lvs on ip:{ip},port:{lvs_port}"
else
echo "fail uncompress   kp+lvs on ip:{ip},port:{lvs_port}"
fi
#install keekalive rpm
rpmexists=`rpm -qa |grep keepalive`
if [ -z ${rpmexists} ];then
yum -y install keepalived  popt*    libnl-devel   gcc

if [ $? -eq 0 ] ;then
echo "success install kp+lvs on ip:{ip},port:{lvs_port}"
else
echo "fail install kp+lvs on ip:{ip},port:{lvs_port}"
fi

fi

ipvsexists=`modprobe -l|grep ipvs`
if [ -z "${ipvsexists}" ]; then
tar xvf ipvsadm-1.26.tar.gz && cd ipvsadm-1.26 && make && make install
if [ $? -eq 0 ] ;then
echo "success install kp+lvs on ip:{ip},port:{port}"
else
echo "kp+lvs exists  on ip:{ip},port:{port}"
fi
fi

#modify keepalive parameter
sed -i "s/lastoneip/${lastoneip}/g" /tmp/Lvs-Keepalived/keepalived.conf
sed -i "s/lvs_role/{lvs_role}/g"   /tmp/Lvs-Keepalived/keepalived.conf
sed -i "s/lvs_network/{lvs_network}/g" /tmp/Lvs-Keepalived/keepalived.conf
sed -i "s/lvs_priority/${lvs_priority}/g" /tmp/Lvs-Keepalived/keepalived.conf
sed -i "s/lvs_vip/{lvs_vip}/g" /tmp/Lvs-Keepalived/keepalived.conf
sed -i "s/lvs_port/{lvs_port}/g" /tmp/Lvs-Keepalived/keepalived.conf

for qsip in {qsiplist};
do
echo ${qsip}
nqsip=`echo ${qsip} |cut -d \: -f 1`
echo ${nqsip}
nqsport=`echo ${qsip} |cut -d \: -f 2`
echo ${nqsport}
sed  -i '/protocol TCP\>/a\ \n\treal_server '${nqsip}'  '${nqsport}' {\n\tweight 1\n\tTCP_CHECK {\n\t\tconnect_timeout 5\n\t\tnb_get_retry 3\n\t\tdelay_before_retry 2\n\t\tconnect_port  '${nqsport}'\n\t\t}\n\t}' /tmp/Lvs-Keepalived/keepalived.conf
done


cp /tmp/Lvs-Keepalived/keepalived.conf /etc/keepalived/keepalived.conf


echo -e "success"

