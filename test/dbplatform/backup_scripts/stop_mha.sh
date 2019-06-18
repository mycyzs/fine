#!/bin/bash
#set -e

mha_manager_list="{0}"
cluster_num={1}
conf_path={2}
echo -n "begin_check:"
check_result="["
for node in $mha_manager_list
do
	masterha_stop --conf=$conf_path/conf/$node/mha.conf > $conf_path/manage/exc.log 2>&1
	manager_num=`ps -ef | grep "master" | grep $node | grep -v grep | wc -l`
	if [[ $manager_num -eq 0 ]];then
		process_status="OFFLINE"
	else
		process_status="ONLINE"
	fi

	if [[ $cluster_num == 1 ]];then
		check_info="{"'"'"cluster_name"'"'":"'"'"$node"'"'","'"'"process"'"'":"'"'"$process_status"'"'"}"
	else
		check_info="{"'"'"cluster_name"'"'":"'"'"$node"'"'","'"'"process"'"'":"'"'"$process_status"'"'"},"
	fi
	cluster_num=$[cluster_num-1]
	check_result=$check_result$check_info
done
check_result=$check_result"]"
echo -n $check_result
echo -n "end_check"
