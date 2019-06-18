#!/bin/bash
#set -e
qsiplist={qsiplist}
lvsip={lvsip}
#modify keepalive parameter
for qsip in {qsiplist};
do
nqsip=`echo ${qsip} |cut -d \: -f 1`
nqsport=`echo ${qsip} |cut -d \: -f 2`

exist_qs=`grep '${nqsip}  ${nqsport}'  /etc/keepalived/keepalived.conf`
if [ -z ${exist_qs} ];then
sed  -i '/protocol TCP\>/a\ \n\treal_server '${nqsip}'  '${nqsport}' {\n\tweight 1\n\tTCP_CHECK {\n\t\tconnect_timeout 5\n\t\tnb_get_retry 3\n\t\tdelay_before_retry 2\n\t\tconnect_port  '${nqsport}'\n\t\t}\n\t}' /etc/keepalived/keepalived.conf

if [ $? -eq 0 ];then
echo  "success modify lvs param on ip:{lvsip}"
else
echo  "fail modify lvs param on ip:{lvsip}"
fi
fi

done



