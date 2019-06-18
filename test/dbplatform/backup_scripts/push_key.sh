#!/bin/bash
#set -e
key_num={0}
key_list="{1}"
for((i=1;i<=$key_num;i++))
do
	key=`echo $key_list | cut -d"*" -f$i`
	echo "$key" >> /home/mhamonitor/.ssh/authorized_keys
done
chmod 600 /home/mhamonitor/.ssh/authorized_keys
chown -R mhamonitor.mhamonitor /home/mhamonitor/.ssh