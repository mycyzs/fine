# -*- coding:utf-8 -*-
import datetime
import json

from django.db.models import Q

from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from common.log import logger
from common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN

# 获取平台所有模型
from home_application.celery_tasks import get_host_info
from home_application.models import Host, Load


def search_init(request):
    try:
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin'
        }
        result = client.cc.search_classifications(param)
        data_list = []
        if result['result']:
            for i in result['data']:
                data_list.append({
                    "id": i['bk_classification_id'],
                    "text": i['bk_classification_name']
                })
        return render_json({'result': True, 'data': data_list})
    except Exception as e:
        logger.error(e)


# 获取该模型分类下的所有模型
def search_objects(request):
    try:
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            'bk_classification_id': 'database'
        }
        result = client.cc.search_all_objects(param)
        data_list = []
        if result['result']:
            for i in result['data']:
                data_list.append({
                    "id": i['bk_obj_id'],
                    "text": i['bk_obj_name']
                })
        return render_json({'result': True, 'data': data_list})
    except Exception as e:
        logger.error(e)


# 获取该模型下所有的实例
def search_inst(request):
    try:
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            'bk_obj_id': 'mssql',
            'condition': {},
            'bk_supplier_account': '0'
        }
        result = client.cc.search_inst(param)
        inst_data = {}
        if result['result']:
            inst_data = {'inst_id': result['data']['info'][0]['bk_inst_id']}
        return render_json({'result': True, 'data': inst_data})
    except Exception as e:
        logger.error(e)


# 根据实例名获取实例详情
def search_inst_detail(request):
    try:
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "bk_obj_id": "mssql",
            "page": {"start": 0, "limit": 0, "sort": "-bk_inst_id"},
            "fields": {},
            "condition": {'bk_inst_name': 'mssql-192.168.169.22'}
        }
        result = client.cc.search_inst_by_object(param)
        inst_data = {}
        if result['result']:
            inst_data = {'inst_id': result['data']['info'][0]['bk_inst_id']}
        return render_json({'result': True, 'data': inst_data})
    except Exception as e:
        logger.error(e)


# 根据实例名获取实例详情
def search_set(request):
    try:
        request_data = json.loads(request.body)
        app_id = request_data['app_id']
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "bk_biz_id": app_id,
            "page": {"start": 0, "limit": 0, "sort": "bk_set_id"},
            "fields": ['bk_set_name', 'bk_set_id'],
            "condition": {}
        }
        result = client.cc.search_set(param)
        data_list = []
        if result['result']:
            data_list = [{'id': i['bk_set_id'], 'text': i['bk_set_name']} for i in result['data']['info']]

        return render_json({'result': True, 'data': data_list})
    except Exception as e:
        logger.error(e)


# 查询所有的业务
def search_app(request):
    try:

        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "fields": [
                "bk_biz_id",
                "bk_biz_name"
            ]
        }
        result = client.cc.search_business(param)
        user_business_list = []
        if result["result"]:
            user_business_list = [
                {"id": i["bk_biz_id"], "text": i["bk_biz_name"]} for i in result["data"]["info"]]
        return render_json({"result": True, "data": user_business_list})
    except Exception as e:
        logger.error(e)


# 查询业务下的所有主机
def search_app_host(request):
    try:
        request_data = json.loads(request.body)
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "ip": {"flag": "bk_host_innerip|bk_host_outerip", "exact": 1, "data": []},

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
                            "value": int(request_data['app_id'])
                        }
                    ]
                }
            ]
        }
        result = client.cc.search_host(kwargs)
        host_list = []
        if result["result"]:
            for i in result['data']['info']:
                host_list.append({
                    'id': i['host']['bk_host_innerip'],
                    'text': i['host']['bk_host_innerip']
                })
        return render_json({"result": True, "data": host_list})
    except Exception as e:
        logger.error(e)


os_type = {'1': 'Linux', '2': 'Windows'}


# 查询不属于该业务下所有主机
def search_all_host(request):
    try:
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "ip": {"flag": "bk_host_innerip|bk_host_outerip", "exact": 1, "data": []},
            "condition": [
                {
                    "bk_obj_id": "biz",
                    "fields": [
                        "default",
                        "bk_biz_id",
                        "bk_biz_name",
                    ],
                    # 根据业务ID查询主机
                    "condition": [{"field": "bk_biz_id", "operator": "$nin", "value": 6}]
                }
            ]
        }
        result = client.cc.search_host(kwargs)
        host_list = []
        if result["result"]:
            for i in result['data']['info']:
                host_list.append({
                    'id': i['host']['bk_host_id'],
                    'text': i['host']['bk_host_innerip']
                })
        return render_json({"result": True, "data": host_list})
    except Exception as e:
        logger.error(e)


# 根据ip查询主机信息
def search_host_by_ip(request):
    try:
        request_data = json.loads(request.body)
        ip = request_data['ip']
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": request.user.username,
            "ip": {"flag": "bk_host_innerip|bk_host_outerip", "exact": 1, "data": [ip] if ip else []},
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
        server_list = []
        if result["result"]:
            for i in result['data']['info']:
                server_list.append({
                    'ip': i['host']['bk_host_innerip'],
                    'server_name': i['host']['bk_host_name'],
                    'app_name': i['biz'][0]['bk_biz_name'],
                    'app_id': i['biz'][0]['bk_biz_id'],
                    'bk_cloud_name': i['host']['bk_cloud_id'][0]['bk_inst_name'],
                    'bk_cloud_id': i['host']['bk_cloud_id'][0]['bk_inst_id'],
                    'os_type': os_type[i['host']['bk_os_type']] if i['host']['bk_os_type'] else ''

                })

        return render_json({"result": True, "data": server_list})
    except Exception as e:
        logger.error(e)


# 饼图
def get_count_obj(request):
    data_list = [
        {'name': "test1", 'y': 10},
        {'name': "test2", 'y': 20}
    ]

    return render_json({'result': True, 'data': data_list})


# 折线图
def get_count(request):
    date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)
    time_now = datetime.datetime.now()
    when_created__gt = str(date_now).split(".")[0]
    time_n = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 存的时候
    # when_created = str(datetime.datetime.now()).split(".")[0]
    # 数据库读取的时候
    # when_created__gt = str(date_now).split(".")[0]

    install_list = [
        {"name": u"本月MySQL新增数", "data": [3, 6, 8, 9]},
        {"name": u"本月Oracle新增数", "data": [1, 4, 7, 10]}
    ]
    return render_json({'result': True, 'data': install_list, 'cat': ['1', '2', '3', '4']})


# 柱状图
def get_count_zhu(request):
    data = [
        {'name': 'Windows服务器', 'data': [1]},
        {'name': 'AD服务器', 'data': [3], 'color': "#4cb5b0"},
        {'name': 'TEST服务器', 'data': [5]}
    ]

    return render_json({'result': True, 'data': data})


def search_host(request):
    request_data = json.loads(request.body)
    ip = request_data['ip']
    hosts = Host.objects.filter(host_ip__icontains=ip)
    ip_list = []
    for i in hosts:
        ip_list.append({
            'id': i.id,
            'host_ip': i.host_ip,
            'host_name': i.host_name,
            'app_name': i.app_name,
            'app_id': i.app_id,
            'cloud_name': i.cloud_name,
            'cloud_id': i.cloud_id,
            'os_type': i.os_type,
            'comment': i.comment
        })
    return render_json({'result': True, 'data': ip_list})


def search_info(request):
    # get_host_info()
    request_data = json.loads(request.body)
    host = Host.objects.get(id=request_data['host_id'])
    try:
        men = json.loads(host.men)
        for d in men:
            d['y'] = int(d['y'])
    except Exception as e:
        men = []
    try:
        disk = json.loads(host.disk)
    except Exception as e:
        disk = []

    x_data = [{'name': '负载数', 'data': []}]
    x_line = []
    date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)
    for i in Load.objects.filter(host=host, created_time__gt=date_now):
        x_data[0]['data'].append(float(i.load_info))
        x_line.append(i.created_time)

    load_data = {
        'data': x_data,
        'x': x_line
    }

    return render_json({'result': True, 'men': men, 'disk': disk, 'load_data': load_data})


def search_load(request):
    request_data = json.loads(request.body)
    start = datetime.datetime.strptime(request_data['start'], "%Y-%m-%d %H:%M:%S")
    end = datetime.datetime.strptime(request_data['end'], "%Y-%m-%d %H:%M:%S")
    host_id = request_data['host_id']
    host = Host.objects.get(id=host_id)
    x_data = [{'name': '负载数', 'data': []}]
    x_line = []
    date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)
    loads = Load.objects.filter(created_time__gt=start, host=host)
    hosts = []
    for l in loads:
        if datetime.datetime.strptime(l.created_time, "%Y-%m-%d %H:%M:%S") < end:
            hosts.append(l)
    for i in hosts:
        x_data[0]['data'].append(float(i.load_info))
        x_line.append(i.created_time)
    load_data = {
        'data': x_data,
        'x': x_line
    }

    return render_json({'result': True, 'load_data': load_data})


def search_hosts(request):
    try:
        request_data = json.loads(request.body)
        set_id = request_data['set_id']
        app_id = request_data['app_id']
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
                    'host_name':i['host']['bk_host_name'],
                    'server_name': i['host']['bk_host_name'],
                    'app_id': app_id,
                    'bk_cloud_name': i['host']['bk_cloud_id'][0]['bk_inst_name'],
                    'bk_cloud_id': i['host']['bk_cloud_id'][0]['bk_inst_id'],
                    'os_type': os_type[i['host']['bk_os_type']] if i['host']['bk_os_type'] else '',
                    'bk_os_name':i['host']['bk_os_name']

                })
        return render_json({"result": True, "data": host_list})
    except Exception as e:
        logger.error(e)
