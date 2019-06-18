# -*- coding:utf-8 -*-
import json
import os
import urllib

import qrcode
from django.http import HttpResponse

import settings
from blueking.component.shortcuts import get_client_by_request
from common.log import logger
from common.mymako import render_json


def test(request):
    return render_json({"username":request.user.username,'result':'ok'})


def search_sys_info(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        return_data = []
        data = {
            "id": "1",
            "sys_name": "二维码",
            "sys_code": "te",
            "owners": "Admin",
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


def search_aa_info(request):
    try:
        qr = qrcode.QRCode(
            version=8,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data("hello mr.wang")
        qr.make(fit=True)
        img = qr.make_image()
        img_path = os.path.join(settings.PROJECT_ROOT,'test.png')
        if not os.path.exists(img_path):
            img.save("test.png")
    except Exception as e:
        pass
    return render_json({"result": True, "data": {}})



def add_sys(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        data = {
            "id": "1",
            "sys_name": "test1",
            "sys_code": "te1",
            "owners": "dd",
            "is_control": "否",
            "department": "dd",
            "comment": "dja",
            "first_owner": "lhf"
        }
        return render_json({"result": True, "data": data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询系统信息失败!!"]})


def open_test(request):
    try:

        imagepath = os.path.join(settings.PROJECT_ROOT, "test.png") # 图片路径
        with open(imagepath, 'rb') as f:
            image_data = f.read()
        return HttpResponse(image_data, content_type="image/png")
    except Exception as e:
        print e


def down_load_picture(request):
    try:

        file_path = os.path.join(settings.PROJECT_ROOT, "test.png")
        file_buffer = open(file_path, 'rb').read()
        response = HttpResponse(file_buffer, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename=' + 'code.png'
        response['Content-Length'] = os.path.getsize(file_path)
        return response
    except Exception as e:
        logger.exception("download file error:{0}".format(e.message))



def modify_sys(request):
    try:
        request_data = json.loads(request.body)
        username = request.user.username
        data = {
            "id": "1",
            "sys_name": request_data['sys_name'],
            "sys_code": request_data['sys_code'],
            "owners": "dkdkdkd",
            "is_control": request_data['is_control'],
            "department": "dd",
            "comment": "dja",
            "first_owner": request_data['first_owner']
        }

        return render_json({"result": True, "data": data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"添加信息失败!!"]})


def delete_sys(request):
    try:
        request_data = json.loads(request.body)
        username = request.user.username

        return render_json({"result": True, "data": {}})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"添加信息失败!!"]})


