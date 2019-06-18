# -*- coding:utf-8 -*-

from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST
import requests
import json
import base64
import time

# 提供给业务管理界面使用的esb接口，其他位置没有使用这个文件
# 获取业务列表
def search_business_message(request):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_business/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_token": request.COOKIES["bk_token"]
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)

    return res

# 获取业务列表,用于周期任务，所以角色固化为admin
def search_business_message_by_admin():
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_business/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin"
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)

    return res



def get_set_list(username, biz_id):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_set/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": biz_id,
        "fields": [
        ],
        "condition": {
        }

    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)
    return res


def get_module_list(username, biz_id, set_id):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_module/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": biz_id,
        "bk_set_id": set_id,
        "fields": [
        ],
        "condition": {

        }

    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)
    return res


# 根据业务id获取ip列表
def get_host_ip_list(username, biz_id):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_host/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "condition": [
            {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": int(biz_id)
                    }
                ]
            }
        ],
        "pattern": ""
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)

    return res


# 快速执行脚本
def fast_use_script(request, bk_biz_id, script_data, ip_list):
    # 默认从django settings中获取APP认证信息：应用ID和安全密钥
    # 默认从django request中获取用户登录态bk_token
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/job/fast_execute_script/"
    kwargs = {
        "bk_app_code": APP_ID,  # appID
        "bk_app_secret": APP_TOKEN,  # appToken
        "bk_token": request.COOKIES["bk_token"],  # 认证token
        "bk_biz_id": bk_biz_id,  # 业务id
        "script_content": base64.b64encode(script_data),  # 实际执行脚本，要求bash64编码
        "script_timeout": 1000,  # 脚本超时时间
        "account": "root",  # 机器执行脚本的账号
        "is_param_sensitive": 0,  # 参数是否敏感
        "script_type": 1,  # 脚本类型：1(shell脚本)、2(bat脚本)、3(perl脚本)、4(python脚本)、5(Powershell脚本)
        "ip_list": ip_list
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)
    id = ""
    if res["result"] != False:
        id = res["data"]["job_instance_id"]
    return id


# 快速获取脚本日志，即执行结果
def quick_get_log(request, bk_biz_id, job_instance_id):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/job/get_job_instance_log/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_token": request.COOKIES["bk_token"],
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id

    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)

    return res
