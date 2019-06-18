#!/bin/bash
#set -e

mha_manager={0}
n_ms_host={1}
n_ms_port={2}
conf_path={3}
echo -n "begin:"
masterha_master_switch --conf=$conf_path/conf/$mha_manager/mha.conf  --master_state=alive --new_master_host=$n_ms_host --new_master_port=$n_ms_port --orig_master_is_new_slave --running_updates_limit=10000 --interactive=0 > $conf_path/manage/exc.log 2>&1
error_num=`cat $conf_path/manage/exc.log | grep -w "error" | wc -l`
correct_num=`cat $conf_path/manage/exc.log | grep -w "completed successfully" | wc -l `
if [[ $error_num -eq 0 && $correct_num -eq 1 ]];then
    echo -n "success"
else
    echo -n "error"
fi
echo -n ":end"

