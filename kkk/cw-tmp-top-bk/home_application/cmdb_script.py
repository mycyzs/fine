# -*- coding:utf-8 -*-




import base64
import json
import os
import time

from blueking.component import client
from blueking.component.shortcuts import get_client_by_user
from common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN, PROJECT_ROOT
from home_application.models import Host


def get_job_by_id(request):
    request_data = json.loads(request.body)
    app_id = request_data['app_id']
    set_id = request_data['set_id']

    client = get_client_by_user(request.user.username)
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": 'admin',
        "ip": {"flag": "bk_host_innerip|bk_host_outerip", "exact": 1, "data": []},
        "condition": [
            {
                "bk_obj_id": "set",
                "fields": [
                    "default",
                    "bk_set_id",
                    "bk_set_name",
                ],
                # 根据业务ID查询主机
                "condition": [{"field": "bk_set_id", "operator": "$eq", "value": int(set_id)}]
            }
        ]
    }
    result = client.cc.search_host(kwargs)
    host_list = []
    if result["result"]:
        for i in result['data']['info']:
            host_list.append({
                'host_ip': i['host']['bk_host_innerip'],
                'host_name': i['host']['bk_host_name'],
                'server_name': i['host']['bk_host_name'],
                'app_id': app_id,
                'bk_cloud_name': i['host']['bk_cloud_id'][0]['bk_inst_name'],
                'bk_cloud_id': i['host']['bk_cloud_id'][0]['bk_inst_id'],
                'bk_os_name': i['host']['bk_os_name']

            })
    for i in host_list:
        if Host.objects.filter(host_ip=i['host_ip']).exists():
            continue

        Host.objects.create(host_ip=i['host_ip'],host_name=i['host_name'],app_id=i['app_id'],cloud_name=i['bk_cloud_name'],cloud_id=i['bk_cloud_id'],app_name=i['host_name'])

    return render_json({'result':True})


# 获取脚本任务Log
def get_ip_log_content(client, username, task_id, biz_id, i=1):
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "job_instance_id": task_id,
        'bk_biz_id':biz_id
    }
    result = client.job.get_job_instance_log(kwargs)
    if result["result"]:
        if result["data"][0]["is_finished"]:
            ip_log_content = []
            for i in result["data"][0]["step_results"]:
                if i["ip_status"] == 9:
                    result_op = True
                else:
                    result_op = False
                for z in i['ip_logs']:
                    ip_log_content.append({
                        'result':result_op,
                        'ip':z['ip'],
                        'bk_cloud_id':z['bk_cloud_id'],
                        'log_content':z['log_content'],
                    })
            return {"result": True, "data": ip_log_content}
        else:
            time.sleep(1)
            return get_ip_log_content(client, username, task_id,kwargs['bk_biz_id'])
    else:
        i += 1
        if i < 5:
            time.sleep(1)
            return get_ip_log_content(client, username, task_id, kwargs['bk_biz_id'])
        else:
            err_msg = "get_logContent_timeout;task_id:%s;err_msg:%s" % (task_id, result["message"])

            return {"result":False, "msg": err_msg}



# 执行脚本接口
def install_mysql_by_script(username, app_id, app_list,script_content, script_type=1, script_timeout=600):
    client = get_client_by_user(username)
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_biz_id": app_id,
        "bk_username": username,
        "script_content": base64.b64encode(script_content),
        "ip_list": app_list,
        "script_type": script_type,
        "account": 'root',
        "script_timeout": script_timeout
    }
    result = client.job.fast_execute_script(kwargs)
    if result["result"]:
        task_id = result["data"]["job_instance_id"]
        time.sleep(2)
        return get_ip_log_content(client, username, task_id, app_id)
    else:
        return {"result": False, "data": result["message"]}


# 读取安装脚本
def get_install_script(instance_info):
    # 获取安装脚本
    install_file_path = os.path.join(PROJECT_ROOT, 'backup_scripts/install_mysql.sh')
    install_scripts = open(install_file_path)
    script_content = install_scripts.read()
    install_scripts.close()
    # 替换脚本的端口和安装包
    return script_content.replace("{0}", str(instance_info['port'])).replace("{1}", instance_info['mysql_package'])



def for_emple(request):
    bk_user = request.user.username
    instance_info = {}
    instance_info["app_id"] = "app_id"
    instance_info["ip"] = 'ip'
    instance_info["source"] = 'source'
    script_content = "ps -ef | grep '\-\-port=3306' | awk -F'--defaults-file=' '{print $2}' | awk '{print $1}'"
    result_data = install_mysql_by_script(bk_user, instance_info, script_content)
    if result_data['result']:
        pass



# 快速分发脚本
def fast_push_file(instance_info, username, install_info):
    kwargs = {
        "app_code": APP_ID,
        "app_secret": APP_TOKEN,
        "username": username,
        "app_id": instance_info['app_id'],
        #源文件主机参数
        "file_source": [
            {
                "account": install_info['server_account'],
                "ip_list": [{
                    "ip": install_info['file_server_ip'],
                    "source": install_info['file_source']
                }],
                "file": install_info['install_path']
            },

        ],
        #目标服务器参数
        "account": username,
        "file_target_path": "/tmp",  # 分发到哪个目录下
        "ip_list": [
            {
                "ip": instance_info['ip'],
                "source": instance_info['source']
            }
        ],
    }
    client = get_client_by_user(username)
    result = client.job.fast_push_file(kwargs)
    if result["result"]:
        task_id = result["data"]["taskInstanceId"]
        time.sleep(2)
        return get_ip_log_content(client, username, task_id)
    else:
        return {"result": False, "data": result["message"]}


def get_push_file(request):
    bk_user = request.user.username
    instance_info = {}
    install_info = {}
    result = fast_push_file(instance_info, bk_user, install_info)
    if result['result']:
        pass