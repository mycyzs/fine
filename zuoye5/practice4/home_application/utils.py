#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.utils import timezone

import settings
import base64
import time, datetime


CONSTANT_PARAM = {
    'bk_app_code': settings.APP_ID,
    'bk_app_secret': settings.APP_TOKEN
}


def get_business(client, params):
    params.update(CONSTANT_PARAM)
    res = client.cc.search_business(params)
    if res['result']:
        return {"result": True, "data": res['data']['info']}
    return {"result": False, "data": res["data"]}


def get_host(client, filter_obj):
    kwargs = {
        "ip": {
            "flag": "bk_host_innerip|bk_host_outerip",
            "exact": 1,
            "data": filter_obj.get('ip_list',[])
        },
        "condition": [
            {"bk_obj_id": "host", "fields": [], "condition": [] },
            {"bk_obj_id": "module", "fields": [], "condition": []},
            {"bk_obj_id": "set", "fields": [], "condition": []},
            {"bk_obj_id": "biz","fields": [],"condition": [{
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": filter_obj["bk_biz_id"]
                    }]},
        ]
    }
    res = client.cc.search_host(kwargs)
    if res['result']:
        return {"result": True, "data": res['data']['info']}
    return {"result": False, "data": res["data"]}


# 快速执行作业
def fast_execute_script(client, bk_biz_id, username, ip_list, script_content, execute_account='root',
                        param_content='', script_timeout=1000):
    """
    快速执行脚本
    :param check_app: 操作的对象，dict，{"app_id":1,"ip_list":[{"ip":"10.0.0.10","bk_cloud_id":0}]}
    :param client: ESB连接客户端，client class
    :param user_name:  有该业务操作权限的用户，str
    :param execute_account: 脚本执行帐号，str
    :param script_content: 脚本执行内容，str
    :param param_content: 脚本参数，str，可不传
    :param script_timeout: 超时时间，int，可不传
    :return: 脚本执行结果，list：[{"ip": '10.0.0.10', "log_content": '123', "bk_cloud_id": 0, "is_success": True}]
    """
    kwargs = {
        "bk_username": username,
        "bk_biz_id": bk_biz_id,
        "script_content": base64.b64encode(script_content),
        "ip_list": ip_list,
        "script_type": 1,
        "account": execute_account,
        "script_param": base64.b64encode(param_content),
        "script_timeout": script_timeout
    }
    kwargs.update(CONSTANT_PARAM)
    result = client.job.fast_execute_script(kwargs)
    if result["result"]:
        job_instance_id = result["data"]["job_instance_id"]
        res_data = get_task_ip_log(client, bk_biz_id, job_instance_id, username)
        return {"result": True, "data": res_data["data"]}
    else:
        return {"result": False, "data": result["message"]}


def get_task_ip_log(client, app_id, task_instance_id, user_name, count=0):
    """
    获取脚本执行结果
    :param client: ESB连接客户端，client class
    :param app_id: 业务ID，int
    :param task_instance_id: 作业实例ID，int
    :param user_name: 有查看该脚本执行结果权限的用户 ,str
    :param count: 已重试的次数，直接调用不传
    :return: 脚本执行结果，list：[{"ip": '10.0.0.10', "log_content": '123', "bk_cloud_id": 0, "is_success": True}]
    """
    kwargs = {
        "bk_username": user_name,
        "bk_biz_id": app_id,
        "job_instance_id": int(task_instance_id)
    }
    kwargs.update(CONSTANT_PARAM)
    i = 0
    while True:
        job_status = client.job.get_job_instance_status(kwargs)
        i += 1
        time.sleep(0.2)
        if i > 2000 or job_status['data']['is_finished']:
            break

    if job_status['result']:
        job_result = client.job.get_job_instance_log(kwargs)
        if job_result['data'][0]['is_finished']:
            res_mes = job_result['data'][0]['step_results'][0]['ip_logs']
            return {'result':True,'data': res_mes}
    return {'result':False, 'data': u'作业执行失败，请稍后再试'}


# 快速分发文件
def fast_push_file(client, ip_list, username, file_target_path, file_source):
    params = {
        'bk_username': username,
        'ip_list': ip_list,
        'file_target_path': file_target_path,
        'file_source': file_source
    }
    params.update(CONSTANT_PARAM)
    client.job.fast_push_file(params)


# 启动作业
# params={'bk_username':username,'bk_job_id':2, 'bk_biz_id': 2}
def excute_job(client, ip_list, params):
    params.update(CONSTANT_PARAM)
    job_detail = client.job.get_job_detail(params)
    if job_detail['code'] != 0:
        return {"result": False, "data": ['获取作业信息失败']}
    steps = job_detail['data']['steps']
    for i in steps:
        i['ip_list'] = ip_list
    params['steps'] = steps
    job_res = client.job.execute_job(params)
    if job_res['code'] != 0:
        return {"result": False, "data": ['获取作业信息失败']}
    job_instance_id = job_res['data']['job_instance_id']
    res = get_task_ip_log(client, params['bk_biz_id'], job_instance_id, params['bk_username'])
    if res['result']:
        return {'result': True, 'data': res['data']}
    return {'result': False, 'data':'执行作业失败'}


# datetime转换为字符串
def datetime_to_str(d_time):
    """
    :param d_time: datetime 对象
    :return: 字符串，格式如：2008-1-1 10:30:15
    """
    return time.strftime("%Y-%m-%d %H:%M:%S")


# 字符串转换为datetime对象
def str_to_datetime(time_str=""):
    """
    :param time_str: 字符串，格式如：2008-1-1 10:30:15
    :return: datetime 对象
    """
    return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

# 获取
def get_categories_minutes():
    categories = []
    for i in xrange(1, 60):
        categories.append((timezone.now() - datetime.timedelta(minutes=i)).strftime('%H:%M'))
    categories.reverse()
    return categories

def get_categories_days():
    pass

# def get_one_server_line_chart_data(i):
#     date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)
#
#     server_performs = ServerPerformance.objects.filter(server_id=i.id, when_created__gt=str(date_now).split(".")[0]).order_by("id")
#     one_obj = [
#         {"name": "cpu", "data": [i.cpu_usage for i in server_performs]},
#         {"name": "mem", "data": [i.mem_usage for i in server_performs]},
#         {"name": "disk", "data": [i.disk_usage for i in server_performs]},
#     ]
#     return {"categories": [i.when_created for i in server_performs], "data": one_obj}


# def get_host_data_mes(host):
#     return_data = [
#         {"name": "cpu", "data":[]},
#         {"name": "mem", "data":[]},
#         {"name": "disk", "data":[]},
#                    ]
#     for i in xrange(60):
#         gt_time = timezone.now() - datetime.timedelta(minutes=i)
#         lt_time = timezone.now() - datetime.timedelta(minutes=i-1)
#         host_data_mes = HostData.objects.filter(when_created__gte=gt_time, when_created__lte=lt_time, host=host)
#         if not host_data_mes:
#             return_data[0]['data'].append(None)
#             return_data[1]['data'].append(None)
#             return_data[2]['data'].append(None)
#         else:
#             return_data[0]['data'].append(host_data_mes[0].cpu_usage)
#             return_data[1]['data'].append(host_data_mes[0].mem_usage)
#             return_data[2]['data'].append(host_data_mes[0].disk_usage)
#     for j in return_data:
#         j['data'].reverse()
#     return return_data
