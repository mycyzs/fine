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
from blueking.component.shortcuts import get_client_by_user
from common.mymako import render_mako_context, render_json
from utils import *
import base64
from models import *
import json
import datetime

def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/js_factory.html')


def search_biz(reqeust):
    username = reqeust.user.username
    client = get_client_by_user(username)
    result = get_business(client, {'bk_username': username})
    return render_json(result)


def create_course(request):
    files_str = base64.b64encode(request.FILES['file'].read())
    title = request.POST['title']
    content = request.POST['content']
    tip = request.POST['tip']
    bk_biz_id = request.POST['bk_biz_id']
    params = {
        'bk_biz_id': bk_biz_id,
        'title': title,
        'tip': tip,
        'content': content,
        'image': files_str
    }
    CourseMes.objects.create(**params)
    return render_json({'result': True})


def search_course_list(request):
    params = json.loads(request.body)
    username = request.user.username
    client = get_client_by_user(username)
    biz_result = get_business(client, {'bk_username': username})
    biz_dict = {i['bk_biz_id']: i['bk_biz_name'] for i in biz_result['data']}
    course_list = CourseMes.objects.filter(bk_biz_id__in=biz_dict.keys(),title__icontains=params['title'])
    return_result = [i.to_dict() for i in course_list]
    for j in return_result:
        j['bk_biz_name'] = biz_dict[j['bk_biz_id']]
    return render_json({'result': True, 'data': return_result})


def get_all_course(request):
    course_list = CourseMes.objects.all()[:10]
    return_result = [i.to_dict() for i in course_list]
    return render_json({'result': True, 'data': return_result})


def add_history(request):
    params = json.loads(request.body)
    course_id = params['id']
    course = CourseMes.objects.get(id=course_id)
    time_now = datetime.datetime.now()
    create_param = {
        "course": course,
        "time": time_now
    }
    History.objects.create(**create_param)
    return render_json({'result': True})


def search_report(request):
    params = json.loads(request.body)
    bk_biz_id = params['bk_biz_id']
    course_list = CourseMes.objects.filter(title__icontains=params['title'])
    if bk_biz_id:
        course_list.filter(bk_biz_id=bk_biz_id)
    return_data = []
    for i in course_list:
        result = get_data_list(i)
        return_data.append(result)

    return render_json({'result':True, 'data': return_data})


def get_data_list(course_obj):
    history_list = History.objects.filter(course=course_obj)
    days_list = get_categories_days()
    count_list = []
    for i in days_list:
        time_first = i + " 00:00:00"
        real_time_first = datetime.datetime.strptime(time_first, "%Y-%m-%d %H:%M:%S")
        time_last = i + " 23:59:59"
        real_time_last = datetime.datetime.strptime(time_last, "%Y-%m-%d %H:%M:%S")
        count = history_list.filter(time__gte=real_time_first, time__lte=real_time_last).count()
        count_list.append(count)
    return {'categories': days_list, 'data': [{'data': count_list, 'name': course_obj.title}]}


def get_categories_days():
    categories = []
    for i in xrange(0, 7):
        categories.append((datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y-%m-%d'))
    categories.reverse()
    return categories


def update_course(request):
    files_str = base64.b64encode(request.FILES['file'].read())
    title = request.POST['title']
    content = request.POST['content']
    tip = request.POST['tip']
    bk_biz_id = request.POST['bk_biz_id']
    course_id = request.POST['id']
    course_obj = CourseMes.objects.get(id=course_id)
    params = {
        'bk_biz_id': bk_biz_id,
        'title': title,
        'tip': tip,
        'content': content,
        'image': files_str
    }
    for x,y in params.items():
        setattr(course_obj, x, y)
    course_obj.save()
    return render_json({'result': True})


def delete_course(request):
    params = json.loads(request.body)
    course_id = params['id']
    course_obj = CourseMes.objects.get(id=course_id)
    course_obj.delete()
    return render_json({'result':True})
