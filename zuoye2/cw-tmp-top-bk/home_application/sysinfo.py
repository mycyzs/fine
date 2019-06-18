# -*- coding:utf-8 -*-
import json

from django.db.models import Q

from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from common.log import logger
from common.mymako import render_json
from conf.default import APP_ID, APP_TOKEN
from home_application.models import Order, OrderList


def test(request):
    return render_json({"username":request.user.username,'result':'ok'})


def search_sys_info(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        # 查询所有自己创建或审批的工单
        orders = Order.objects.filter(Q(creator=username, status__in=['created', 'submit']) | Q(checker=username, status='checking'))

        # 根据筛选条件
        if request_data["selected_id"] == 'all':
            request_data["selected_id"] = ''
        orders = orders.filter(order_name__icontains=request_data["order_name"], checker__icontains=request_data["checker"],
                               status__contains=request_data["selected_id"]).exclude(status='checked')

        return_data = []
        for order in orders:
            return_data.append({
                'order_id': order.id,
                "order_name": order.order_name,
                "checker": order.checker,
                "status": order.get_status(),
                "content": order.content,
                "is_submit": 'true' if order.status == 'submit' or order.status == 'checking' else 'false',
                "is_deleted": 'true' if order.status == 'created' or order.status == 'submit' else 'false',
                "is_checker": 'true' if order.status == 'checking' else 'false',
            })
        return render_json({"result": True, "data": return_data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询工单信息失败!!"]})


def add_order(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        data = {
            "order_name": request_data["order_name"],
            "creator": username,
            "checker": request_data["check_owner"],
            "content": request_data["content"],
            "status": request_data["status"]

        }
        new_order = Order.objects.create(**data)

        # 如果是提交则增加一条工单
        if request_data['status'] == 'submit':
            data['status'] = 'checking'
            Order.objects.create(**data)

        data["status"] = new_order.get_status()
        data["order_id"] = new_order.id
        data["is_submit"] = 'true' if request_data['status'] == 'submit' else 'false'
        data["is_deleted"] = 'true'
        return render_json({"result": True, "data": data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"新增工单失败!!"]})


def modify_sys(request):
    try:
        request_data = json.loads(request.body)
        username =  request.user.username
        data = {
            "order_name": request_data["order_name"],
            "checker": request_data["check_owner"],
            "content": request_data["content"],
            "status": request_data["status"]
        }

        Order.objects.filter(id=request_data["order_id"]).update(**data)

        if request_data['status'] == 'submit':
            data['status'] = 'checking'
            data['creator'] = username
            Order.objects.create(**data)
        order = Order.objects.get(id=request_data["order_id"])
        data["status"] = order.get_status()
        data["is_submit"] = 'true' if request_data['status'] == 'submit' else 'false'

        return render_json({"result": True, "data": data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"修改信息失败!!"]})


def delete_sys(request):
    try:
        request_data = json.loads(request.body)
        Order.objects.filter(id=request_data['order_id']).delete()

        return render_json({"result": True, "data": {}})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"删除工单失败!!"]})


def agree(request):
    try:
        request_data = json.loads(request.body)
        order = Order.objects.get(id=request_data['order_id'])
        order.status = 'checked'
        order.save()

        OrderList.objects.create(check_status='agree', comment=u'同意', order=order)

        return render_json({"result": True, "data": {}})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"审核失败!!"]})


def refuse(request):
    try:
        request_data = json.loads(request.body)
        order = Order.objects.get(id=request_data['order_id'])
        order.status = 'checked'
        order.save()

        OrderList.objects.create(check_status='refuse', comment=request_data['comment'], order=order)

        return render_json({"result": True, "data": {}})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"审核失败!!"]})


def search_order_info(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        # 查询所有自己创建或审批的工单
        orders = OrderList.objects.filter(Q(order__checker=username) | Q(order__creator=username))

        # 根据筛选条件
        if request_data["selected_id"] == 'all':
            request_data["selected_id"] = ''
        orders = orders.filter(check_status__contains=request_data['selected_id'], order__order_name__contains=request_data['order_name'],
                               order__checker__contains=request_data['checker'])

        return_data = []
        for order in orders:
            return_data.append({
                "order_name": order.order.order_name,
                "checker": order.order.checker,
                "status": order.get_check_status(),
                "comment": order.comment,

            })
        return render_json({"result": True, "data": return_data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询历史工单信息失败!!"]})


# 查询所有用户

def get_all_user(request):

    client = get_client_by_user(request.user.username)

    param = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": "admin"
    }

    result = client.bk_login.get_all_user(param)
    return_data = []
    if result['result']:
        for user in result['data']:
            if user['bk_username'] == request.user.username:
                continue
            return_data.append({'id': user['bk_username'], 'text': user['bk_username']})
        data = {'result': True, 'data': return_data}

    else:
        data = {'result': False, 'msg': [u"查询用户信息失败!!"]}

    return render_json(data)