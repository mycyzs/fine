# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime
import json

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task

from common.log import logger
from home_application.cmdb_script import install_mysql_by_script
from home_application.models import Host, Load


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y


def execute_task():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))


@periodic_task(run_every=crontab(minute='*/1', hour='*', day_of_week="*"))
def get_host_info():
    for app in Host.objects.values('app_id').distinct():
        username = 'admin'
        script_content = '''
                $(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
                echo @@@@@@@@@@
                $(df -h | awk '$NF=="/"{printf "%s", $5}')
                echo @@@@@@@@@@
                $(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
                '''
        app_list = [{'ip': i.host_ip, 'bk_cloud_id': i.cloud_id} for i in Host.objects.filter(app_id=app['app_id'])]
        res = install_mysql_by_script(username, app['app_id'], app_list, script_content)
        if res['result']:
            parse_data(res['data'])


def parse_data(data):
    try:
        for server in data:
            get_log_list = server['log_content'].split('@@@@@@@@@@')
            load_data = get_log_list[0].split(':')[1]
            disk_data = get_log_list[1].split(':')[1]
            cpu_data = get_log_list[2].split(':')[1]

            host = Host.objects.get(host_ip=server['ip'])
            tm = str(datetime.datetime.now()).split('.')[0]
            load = load_data.split()[1]
            Load.objects.create(created_time=tm, load_info=load, host=host)

            host.men = json.dumps(make_men_data(disk_data))
            host.disk = json.dumps(make_disk_data(disk_data))
            host.save()
    except Exception as e:
        logger.error(e)


def make_men_data(data):
    use_list = []
    use = {"name": "已使用", "y": ""}
    free = {"name": "剩余", "y": ""}
    for i in data.split('\n'):
        if i.split().__len__() == 7 and 'Mem' in i:
            mid_list = i.split()
            use['y'] = mid_list[2]
            free['y'] = mid_list[3]
    use_list.append(use)
    use_list.append(free)
    return use_list


def make_disk_data(data):
    title_list = ['Filesystem', 'Size', 'Used', 'Avail', 'Use', 'Mounted']
    ret_data = []
    line_index = 0
    for i in data.split('\n'):
        ret = {}
        if i.split().__len__() == 6:
            if line_index == 0:
                pass
            else:
                mid_val_list = i.split()
                for index in xrange(6):
                    ret[title_list[index]] = mid_val_list[index]
                ret_data.append(ret)
            line_index += 1
    return ret_data
