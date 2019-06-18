# -*- coding: utf-8 -*-

from common.mymako import render_mako_context,render_json
from celery_tasks import *
import json
import sys
from django.http import HttpResponse
from django.db.models import Q
from home_application.sys_manage import *

reload(sys)
sys.setdefaultencoding('utf-8')


def home(request):
    """
    首页
    """
    # get_monitor()
    return render_mako_context(request, '/home_application/js_factory.html')

def test(request):
    try:
        return render_json({'result': 'ok', 'username':request.user.username })
    except Exception,e:
        return render_json({'result':'false','error':str(e)})



def get_server_list(request):
    try:
        ret = list(Server.objects.all().values())
        return render_json({'result': True, 'data':ret})
    except Exception,e:
        return render_json({'result':False,'error':str(e)})


def get_biz_list(request):
    try:
        ret = search_business(request.user.username)
        return render_json({'result': True, 'data':ret})
    except Exception,e:
        return render_json({'result':False,'error':str(e)})


def get_server_by_biz(request):
    try:
        biz_id = json.loads(request.body).get('id','')
        ret = get_host_ip_list(biz_id)
        return render_json({'result': True, 'data':ret})
    except Exception,e:
        return render_json({'result':False,'error':str(e)})


def add_server(request):
    try:
        get_data = json.loads(request.body)
        up =json.loads(get_data['bk_host_innerip'])
        if Server.objects.filter(bk_host_innerip=up['bk_host_innerip'],bk_cloud_id=up['bk_cloud_id']).exists():
            return render_json({'result':False,'error':u'您添加的ip已存在'})
        up['creator'] = request.user.username
        Server.objects.create(**up)
        return render_json({'result': True})
    except Exception,e:
        return render_json({'result':False,'error':u'添加失败：'+str(e)})

def del_server(request):
    try:
        get_data = json.loads(request.body)
        Server.objects.filter(id=get_data['id']).delete()
        return render_json({'result': True})
    except Exception,e:
        return render_json({'result':False,'error':u'删除失败：'+str(e)})

def get_server_monitor(request):
    try:
        get_data = json.loads(request.body)
        server_obj = Server.objects.get(id=get_data['id'])
        try:
            mem_data = json.loads(server_obj.men)
        except:
            mem_data = {}
        try:
            dis_data = json.loads(server_obj.disk)
        except:
            dis_data = {}
        return render_json({'result': True,'line':line_data(server_obj),'mem_data':mem_data,'dis_data':dis_data})
    except Exception,e:
        return render_json({'result':False,'error':u'删除失败：'+str(e)})

def line_data(server_obj):
    ret = []
    x_ret = []
    for i in server_obj.monitor_set.all()[0:60]:
        x_ret.append(i.create_time)
        ret.append(float(i.load))
    return {'data':ret,'title':x_ret}