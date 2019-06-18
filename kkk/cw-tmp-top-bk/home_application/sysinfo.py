# -*- coding:utf-8 -*-
import json

from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from common.log import logger
from common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN
from home_application.models import Host


def search_sys_info(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        return_data = []
        data = {
            "id": "1",
            "sys_name": "test",
            "sys_code": "te",
            "owners": "dd",
            "is_control": "否",
            "department": "dd",
            "comment": "dja",
            "first_owner": "cyz"
        }
        return_data.append(data)
        return render_json({"result": True, "data": return_data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询系统信息失败!!"]})


os_type = {'1': 'Linux', '2': 'Windows'}

def add_sys(request):
    try:
        request_data = json.loads(request.body)
        ip = request_data['server_ip']
        if Host.objects.filter(host_ip=ip).exists():
            return render_json({'result':False,'msg':'ip已存在'})
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": request.user.username,
            "ip": {"flag": "bk_host_innerip|bk_host_outerip", "exact": 1, "data": [ip]},
            "condition": [
                {
                    "bk_obj_id": "biz",
                    "fields": [
                        "default",
                        "bk_biz_id",
                        "bk_biz_name",
                    ],
                    "condition": []
                }
            ]
        }
        result = client.cc.search_host(kwargs)
        ip_list=[]
        if result["result"]:
            for i in result['data']['info']:
                server_list={
                    'host_ip': i['host']['bk_host_innerip'],
                    'host_name': i['host']['bk_host_name'],
                    'app_name': i['biz'][0]['bk_biz_name'],
                    'app_id': i['biz'][0]['bk_biz_id'],
                    'cloud_name': i['host']['bk_cloud_id'][0]['bk_inst_name'],
                    'cloud_id': i['host']['bk_cloud_id'][0]['bk_inst_id'],
                    'os_type': os_type[i['host']['bk_os_type']] if i['host']['bk_os_type'] else '',
                    'comment':request_data['comment']

                }
                h = Host.objects.create(**server_list)
                server_list['id']=h.id
                ip_list.append(server_list)
            return render_json({"result": True,'data':ip_list})
        else:
            return render_json({'result':False,'msg':'主机添加失败'})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询系统信息失败!!"]})


def modify_sys(request):
    try:
        request_data = json.loads(request.body)
        id = request_data['id']
        comment = request_data['comment']
        Host.objects.filter(id=id).update(comment=comment)
        h = Host.objects.get(id=id)
        data = {
            'comment':h.comment
        }
        return render_json({"result": True,'data':data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"添加信息失败!!"]})


def delete_sys(request):
    try:
        request_data=json.loads(request.body)
        id=request_data['id']
        Host.objects.get(id=id).delete()

        return render_json({"result": True, "data": {}})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"添加信息失败!!"]})


