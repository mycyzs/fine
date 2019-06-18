# -*- coding: utf-8 -*-
from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST
import datetime
import time
import base64

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


# 快速执行脚本
def fast_execute_script(check_app, client, user_name, execute_account, script_content, param_content='',
                        script_timeout=1000):
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
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_biz_id": check_app["app_id"],
        "bk_username": user_name,
        "script_content": base64.b64encode(script_content),
        "ip_list": check_app["ip_list"],
        "script_type": 1,
        "account": execute_account,
        "script_param": base64.b64encode(param_content),
        "script_timeout": script_timeout
    }
    result = client.job.fast_execute_script(kwargs)
    if result["result"]:
        return {"result": True, "data": result["data"]["job_instance_id"]}

    else:
        return {"result": False, "data": result["message"]}


# 获取执行脚本日志
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
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": user_name,
        "bk_biz_id": app_id,
        "job_instance_id": int(task_instance_id)
    }
    result = client.job.get_job_instance_log(kwargs)
    if not result["result"]:
        count += 1
        if count > 5:
            # logger.error(result["message"])
            return []
        time.sleep(10)
        return get_task_ip_log(client, app_id, task_instance_id, user_name, count)
    if result["data"][0]["is_finished"]:
        log_content = []
        for i in result["data"][0]["step_results"]:
            log_content += [{"ip": u["ip"], "log_content": u["log_content"], "bk_cloud_id": u["bk_cloud_id"],
                             "is_success": i['ip_status'] == 9} for u in
                            i["ip_logs"]]
        return log_content
    time.sleep(10)
    return get_task_ip_log(client, app_id, task_instance_id, user_name)


# 根据用户名查询业务
def search_business_by_user(client, username):
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username
    }
    res = client.cc.search_business(kwargs)
    return res


# 根据业务和IP列表查询主机
def search_host_by_ip(client, biz_id, ip_list=[]):
    kwargs = {
        "ip": {
            "flag": "bk_host_innerip|bk_host_outerip",
            "exact": 1,
            "data": ip_list
        },
        "condition": [
            {
                "bk_obj_id": "biz",
                "fields": [
                    "default",
                    "bk_biz_id",
                    "bk_biz_name",
                ],
                # 根据业务ID查询主机
                "condition": [
                    {
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": int(biz_id)
                    }
                ]
            }
        ]
    }
    result = client.cc.search_host(kwargs)
    return result
