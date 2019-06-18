# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
import requests
from home_application.models import *
import StringIO
import xlwt
import xlrd
from django.http import HttpResponse
import time
import os
def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html', {"data": "this is test"})


def demo(request):
    return render_mako_context(request, '/home_application/demo.html')

def search(request):
    ret = list(User.objects.all().values())
    return render_json({'result':True,'data':ret})

def down_demo(request):
    sio = StringIO.StringIO()
    ws = xlwt.Workbook()
    mySheet = ws.add_sheet('A Test Sheet')
    mySheet.write(0,0,u'用户名')
    mySheet.write(0,1,u'邮箱')
    mySheet.write(0,2,u'部门')
    mySheet.write(1, 0, u'roger')
    mySheet.write(1, 1, u'roger@canway.net')
    mySheet.write(1, 2, u'产品研发部')
    ws.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='APPLICATION/OCTET-STREAM')
    response['Content-Disposition'] = 'attachment; filename=demo.xls'
    return response

def up_excel(request):
    name = 'tests%s.xlsx' % (time.time())
    file = open(name, 'wb')
    file.write(request.FILES['files'].read())
    file.close()
    data = xlrd.open_workbook(name)
    table = data.sheets()[0]
    nrows = table.nrows
    for index in range(1,nrows):
        row_list = table.row_values(index)
        up = {
            'name':row_list[0],
            'mail':row_list[1],
            'department':row_list[2],
        }
        if User.objects.filter(name=up['name']).exists():
            User.objects.filter(name=up['name']).update(**up)
        else:
            User.objects.create(**up)
    os.remove(name)
    return render_json({'result':True})

def down_excel(request):
    sio = StringIO.StringIO()
    ws = xlwt.Workbook()
    mySheet = ws.add_sheet('A Test Sheet')
    mySheet.write(0,0,u'用户名')
    mySheet.write(0,1,u'邮箱')
    mySheet.write(0,2,u'部门')
    row_index = 1
    for i in User.objects.all().values():
        mySheet.write(row_index, 0, i['name'])
        mySheet.write(row_index, 1, i['mail'])
        mySheet.write(row_index, 2, i['department'])
    ws.save(sio)
    sio.seek(0)
    response = HttpResponse(sio.getvalue(), content_type='APPLICATION/OCTET-STREAM')
    response['Content-Disposition'] = 'attachment; filename=demo.xls'
    return response