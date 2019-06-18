# -*- coding: utf-8 -*-
from celery import task
from celery.schedules import crontab
from celery.task import periodic_task
from home_application.models import *
from common.log import logger
from home_application.sys_manage import *
import sys

import json

reload(sys)
sys.setdefaultencoding("utf-8")


# """
# celery 任务示例
#
# 本地启动celery命令: python  manage.py  celery  worker  --settings=settings
# 周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
# """
@periodic_task(run_every=crontab(minute='*/1', hour='*', day_of_week="*"))
def get_monitor():
    for biz in Server.objects.values('bk_biz_id').distinct():
        username = 'admin'
        script_content = '''
        cat /proc/loadavg
        echo @@@@@@@@@@
        free -m
        echo @@@@@@@@@@
        df -h
        '''
        mid_data = {'bk_biz_id': biz['bk_biz_id'],
                    'ip_list': [{'ip': i['bk_host_innerip'], 'bk_cloud_id': i['bk_cloud_id']} for i in Server.objects.filter(bk_biz_id = biz['bk_biz_id']).values()],
                    'account': 'root'}
        res = fast_script(username,mid_data,script_content,)
        if res['result']:
            get_res = get_ip_log_content(username, biz['bk_biz_id'],res['data'])
            if get_res['result']:
                make_server_monitor(get_res['data'])
            else:
                logger.error(u'获取脚本日志失败' + str(get_res))
        else:
            logger.error(u'快速执行脚本失败'+str(res))

def make_server_monitor(data):
    create_list = list()
    for server in data:
        try:
            if server['result']:
                get_log_list = server['log_content'].split('@@@@@@@@@@')
                load_data = get_log_list[0]
                men_data = get_log_list[1]
                disk_data = get_log_list[2]
                server_obj = Server.objects.get(bk_cloud_id=server['bk_cloud_id'],bk_host_innerip=server['ip'])
                create_list.append(monitor(**{
                    'create_time':time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                    'load':make_load_data(load_data),
                    'server_id':server_obj.id,
                }))
                server_obj.men = json.dumps(make_men_data(men_data))
                server_obj.disk = json.dumps(make_disk_data(disk_data))
                server_obj.save()
        except Exception,e:
            logger.exception(u'处理性能数据失败')
    monitor.objects.bulk_create(create_list)

def make_load_data(load_data):
    return load_data.split()[1]

def make_men_data(men_data):
    ret = {'used':'','free':''}
    for i in men_data.split('\n'):
        if i.split().__len__()==7 and 'Mem' in i:
            mid_list = i.split()
            ret['used']=mid_list[1]
            ret['free']=mid_list[2]
    return ret

def make_disk_data(disk_data):
    title_list = ['Filesystem','Size','Used','Avail','Use','Mounted']
    ret_data = []
    line_index = 0
    for i in disk_data.split('\n'):
        ret = {}
        if i.split().__len__()==6:
            if line_index==0:
                pass
            else:
                mid_val_list = i.split()
                for index in xrange(6):
                    ret[title_list[index]] = mid_val_list[index]
                ret_data.append(ret)
            line_index+=1
    return ret_data