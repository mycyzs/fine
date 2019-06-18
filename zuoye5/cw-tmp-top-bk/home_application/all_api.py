# -*- coding:utf-8 -*-
import copy
import datetime
import time

from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from common.log import logger
from common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN


# 获取平台所有模型
from home_application.models import Book, Total


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
        return render_json({'result':True,'data':data_list})
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
            'bk_classification_id':'database'
        }
        result = client.cc.search_all_objects(param)
        data_list = []
        if result['result']:
            for i in result['data']:
                data_list.append({
                    "id": i['bk_obj_id'],
                    "text": i['bk_obj_name']
                })
        return render_json({'result':True,'data':data_list})
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
            'bk_obj_id':'mssql',
            'condition':{},
            'bk_supplier_account':'0'
        }
        result = client.cc.search_inst(param)
        inst_data = {}
        if result['result']:
            inst_data = {'inst_id':result['data']['info'][0]['bk_inst_id']}
        return render_json({'result':True,'data':inst_data})
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
            inst_data = {'inst_id':result['data']['info'][0]['bk_inst_id']}
        return render_json({'result':True,'data':inst_data})
    except Exception as e:
        logger.error(e)


# 查询所有的业务
def search_buseness(request):
    try:
        client = get_client_by_user(request.user.username)
        param = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin'
        }
        result = client.cc.search_business(param)
        user_business_list = []
        if result["result"]:
            user_business_list = [
                {"id": i["bk_biz_id"], "text": i["bk_biz_name"]} for i in result["data"]["info"]

            ]
        return render_json({"result": True, "data": user_business_list})
    except Exception as e:
        logger.error(e)


# 查询业务下的所有主机
def search_app_host(request):
    try:
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "ip" : {"flag": "bk_host_innerip|bk_host_outerip","exact": 1,"data": []},

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
                        "value": 2
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
                    'id':i['host']['bk_host_id'],
                    'text':i['host']['bk_host_innerip'],
                    'app_id': i['biz'][0]['bk_biz_id'],
                    'cloud_id': i['host']['bk_cloud_id'][0]['id']
                })
        return render_json({"result": True, "data": host_list})
    except Exception as e:
        logger.error(e)


# 查询不属于该业务下所有主机
def search_all_host(request):
    try:
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "ip" : {"flag": "bk_host_innerip|bk_host_outerip","exact": 1,"data": []},
            "condition": [
                {
                    "bk_obj_id": "biz",
                    "fields": [
                        "default",
                        "bk_biz_id",
                        "bk_biz_name",
                    ],
                    # 根据业务ID查询主机
                    "condition": [{"field":"bk_biz_id","operator":"$nin","value":6}]
                }
            ]
        }
        result = client.cc.search_host(kwargs)
        host_list = []
        if result["result"]:
            for i in result['data']['info']:
                host_list.append({
                    'id':i['host']['bk_host_id'],
                    'text':i['host']['bk_host_innerip']
                })
        return render_json({"result": True, "data": host_list})
    except Exception as e:
        logger.error(e)

os_type = {'1':'Linux','2':'Windows'}


# 根据ip查询主机信息
def search_host_by_ip(request):
    try:
        client = get_client_by_user(request.user.username)
        kwargs = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": 'admin',
            "ip" : {"flag": "bk_host_innerip|bk_host_outerip","exact": 1,"data": ['192.168.165.51']},
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
        d={}
        if result["result"]:
            d = {}

        return render_json({"result": True, "data": d})
    except Exception as e:
        logger.error(e)


# 饼图
def get_count_obj(request):
    data_list = [
        {'name':"test1",'y':10},
        {'name':"test2",'y':20}
    ]

    return render_json({'result':True,'data':data_list})


# 折线图
def get_count(request):
    # date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)
    # time_now = datetime.datetime.now()
    # when_created__gt = str(date_now).split(".")[0]
    # time_n = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    # 存的时候
    # when_created = str(datetime.datetime.now()).split(".")[0]
    # 数据库读取的时候
    # when_created__gt = str(date_now).split(".")[0]
    now = int(time.strftime('%Y%m%d', time.localtime()))
    books = Book.objects.all()
    date = [str(now-6), str(now-5), str(now-4), str(now-3), str(now-2), str(now-1), str(now)]

    obj = {}
    for b in books:
        date_data = []
        for d in date:
            try:
                to = Total.objects.get(book=b, date=d)
                num = to.sum
            except Exception as e:
                num = 0
            finally:
                date_data.append(num)
        obj[str(b.id)] = {"name": b.name, "data": [{'data':copy.deepcopy(date_data), 'name': "访客量"}], 'cat': date}

    # install_list = [
    #     {"name": u"访客量", "data": [1,4,7,10]}
    # ]
    return render_json({'result': True, 'data': obj})



def get_count_zhu(request):
    data = [
        {'name': 'Windows服务器', 'data': [1]},
        {'name': 'AD服务器', 'data': [3], 'color': "#4cb5b0"},
        {'name': 'TEST服务器', 'data': [5]}
    ]

    return render_json({'result':True,'data':data})