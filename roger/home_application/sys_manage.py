# -*- coding: utf-8 -*-
from conf.default import *
import requests
import json
from common.log import logger
import base64
import time

def search_business(user='admin'):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_business/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": user
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)
    if res['result']:
        ret = [{'bk_biz_id':i['bk_biz_id'],'bk_biz_name':i['bk_biz_name']} for i in res['data']['info']]
        return ret
    else:
        logger.error(u'获取业务失败'+str(res))
        return []


def get_host_ip_list(biz_id,username='admin'):
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
    if res['result']:
        ret = []
        for i in res['data']['info']:
            bk_os_type = 'Linux'
            if i['host']["bk_os_type"] == u'1':
                bk_os_type = "Linux"
            elif i['host']["bk_os_type"] == u'2':
                bk_os_type = "Windows"
            mid_dict = {
                'bk_host_innerip':i['host']['bk_host_innerip'],
                'bk_host_name':i['host']['bk_host_name'],
                'bk_cloud_id':i['host']['bk_cloud_id'][0]['bk_inst_id'],
                'bk_inst_name':i['host']['bk_cloud_id'][0]['bk_inst_name'],
                'bk_os_type':bk_os_type,
                'bk_biz_id':i['biz'][0]['bk_biz_id'],
                'bk_biz_name':i['biz'][0]['bk_biz_name'],
            }
            ret.append(mid_dict)
        return ret
    else:
        logger.error(u'获取服务器失败'+str(res))
        return []



def fast_script(username, server, script_content, script_type=1, script_timeout=3600):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/job/fast_execute_script/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": server["bk_biz_id"],
        "script_content": base64.b64encode(script_content),
        "script_timeout": script_timeout,
        "account": server["account"],
        "script_type": script_type,
        "ip_list": server["ip_list"],
    }
    res_json = requests.post(url=URL, json=kwargs,verify=False)
    res = json.loads(res_json.content)
    if res['result']:
        return {"result": True, "data": res['data']['job_instance_id']}
    else:
        logger.error(u'执行脚本失败'+str(res))
        return {"result": False, "data": res}

def get_ip_log_content(username, bk_biz_id,job_instance_id, i=1):
    URL = BK_PAAS_HOST + "/api/c/compapi/v2/job/get_job_instance_log/"
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id,
    }
    res_json = requests.post(url=URL, json=kwargs, verify=False)
    result = json.loads(res_json.content)
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
            return get_ip_log_content(username, bk_biz_id,job_instance_id)
    else:
        i += 1
        if i < 5:
            time.sleep(5)
            return get_ip_log_content(username, bk_biz_id,job_instance_id, i)
        else:
            err_msg = "get_logContent_timeout;task_id:%s;err_msg:%s" % (job_instance_id, result["message"])
            return {"result": False, "data": err_msg}