#!/bin/bash
#set -e

mha_manager_list="{0}"
cluster_num={1}
conf_path={2}
echo -n "begin_check:"
check_result="{"
for node in $mha_manager_list
do
    mha_manager_num=`ps -ef | grep $node | grep -v grep | wc -l`
    if [[ $mha_manager_num -ge 1 ]];then
        process_status="ONLINE"
    else
        process_status="OFFLINE"
    fi

    masterha_check_ssh --conf=$conf_path/test/$node/conf/mha.conf > $conf_path/test/$node/manage/exc.log 2>&1
    ssh_status=`cat $conf_path/test/$node/manage/exc.log | grep "All SSH connection tests passed successfully" | wc -l`
    ssh_test_status=1
    ssh_ip_list=`cat $conf_path/test/$node/conf/mha.conf | grep "hostname" | grep -v "^#" | cut -d "=" -f2`
    ssh_port=`cat $conf_path/test/$node/conf/mha.conf | grep "ssh_port" | grep -v "^#" | cut -d "=" -f2`
    for ssh_ip in $ssh_ip_list
    do
	    ssh -p$ssh_port -o ConnectTimeout=3 -o NumberOfPasswordPrompts=0 -o StrictHostKeyChecking=no mhamonitor@$ssh_ip "pwd" > /dev/null 2>&1
	    if [[ $? != 0 ]];then
	        ssh_test_status=0
	        break
	    fi
    done
    if [[ $ssh_status -eq 1 && $ssh_test_status -eq 1 ]];then
	    ssh_status="ONLINE"
    else
	    ssh_status="OFFLINE"
    fi

    masterha_check_repl --conf=$conf_path/test/$node/conf/mha.conf > $conf_path/test/$node/manage/exc.log 2>&1
    repl_status=`cat $conf_path/test/$node/manage/exc.log | grep "MySQL Replication Health is OK" | wc -l`
    if [[ $repl_status -eq 1 ]];then
	    repl_status="ONLINE"
    else
	    repl_status="OFFLINE"
    fi

    if [[ $cluster_num == 1 ]];then
        check_info='"'"$node"'"'":{"'"'"process_status"'"'":"'"'"$process_status"'"'","'"'"ssh_status"'"'":"'"'"$ssh_status"'"'","'"'"repl_status"'"'":"'"'"$repl_status"'"'"}"
    else
        check_info='"'"$node"'"'":{"'"'"process_status"'"'":"'"'"$process_status"'"'","'"'"ssh_status"'"'":"'"'"$ssh_status"'"'","'"'"repl_status"'"'":"'"'"$repl_status"'"'"},"
    fi
    cluster_num=$[cluster_num-1]
    check_result=$check_result$check_info
done
check_result=$check_result"}"
echo -n $check_result
echo -n "end_check"