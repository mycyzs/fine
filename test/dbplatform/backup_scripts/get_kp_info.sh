#!/bin/bash
#set -e
ip={ip}
qsvip={ddbip}
qsport={ddbport}
network={network_name}
role={role}

#test keep.comf exists
keepalived=/etc/keepalived/keepalived.conf
keepalivedstatus=`ps -ef |grep keepalived |grep -v grep |wc -l`

if [  ! -f ${keepalived} ]  ||  [ ${keepalivedstatus} -eq 0 ] ;then
echo -e  "keepalived.conf not exists or keepalived not running"
exit 1
fi

#get vip and port
vipport=`more /etc/keepalived/keepalived.conf |grep virtual_server`
vip=`echo ${vipport} | cut -d ' ' -f 2`
port=`echo ${vipport} | cut -d ' ' -f 3`
echo -e vip:${vip}
echo -e port:${port}

#get keep role
keeprole=`more /etc/keepalived/keepalived.conf |grep state`
kprole=`echo ${keeprole} | cut -d ' ' -f 2`
echo -e role:${kprole}

#get vip bond network
keepnetwork=`more /etc/keepalived/keepalived.conf |grep interface`
vipbondnetwork=`echo ${keepnetwork} | cut -d ' ' -f 2`
echo -e vipbondnetwork:${vipbondnetwork}


if  [ $? -eq 0 ]; then
echo "success get kp info  on ip:{ip},vip:${qsvip},port:${qsport}"
fi