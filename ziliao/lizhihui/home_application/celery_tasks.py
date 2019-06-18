# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task

from blueking.component.shortcuts import get_client_by_user
from home_application.esb_helper import *
from home_application.models import *


@periodic_task(run_every=crontab(minute='*', hour='*', day_of_week="*"))
def get_servers_perform():
    app_list = Servers.objects.all().values("app_id", "created_by").distinct()
    run_apps = []
    for i in app_list:
        servers = Servers.objects.filter(app_id=i["app_id"], is_deleted=False)
        one_app = {
            "app_id": i["app_id"],
            "ip_list": [{"ip": u.ip_address, "bk_cloud_id": u.cloud_id} for u in servers],
        }
        client = get_client_by_user(i["created_by"])
        result = get_server_perform(client, one_app, i["created_by"])
        if result["result"]:
            run_apps.append({"app_id": i["app_id"], "job_instance_id": result["data"], "username": i["created_by"]})
    performance_list = []
    for i in run_apps:
        client = get_client_by_user(i["username"])
        one_app_result = get_task_ip_log(client, i["app_id"], i["job_instance_id"], i["username"])
        performance_list += create_server_perform(one_app_result, i["app_id"])
    ServerPerformance.objects.bulk_create(
        performance_list, batch_size=500
    )


def get_server_perform(client, check_app, username):
    script_content = """#!/bin/bash

    MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
    DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}')
    CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
    DATE=$(date "+%Y-%m-%d %H:%M:%S")
    echo -e "$DATE|$MEMORY|$DISK|$CPU"
    """
    script_account = "root"
    result = fast_execute_script(check_app, client, username, script_account, script_content)
    return result


def format_log_content(log_content):
    log_result = log_content.strip().split("|")
    one_obj = {
        "mem_usage": log_result[1].strip("%"),
        "disk_usage": log_result[2].strip("%"),
        "cpu_usage": log_result[3].strip("%"),
    }
    return one_obj


def create_server_perform(one_app_result, app_id):
    performance_list = []
    for i in one_app_result:
        if not i["is_success"]:
            continue
        server_result = format_log_content(i["log_content"])
        server = Servers.objects.get(app_id=app_id, ip_address=i["ip"], cloud_id=i["bk_cloud_id"])
        performance_list.append(ServerPerformance(
            server_id=server.id,
            cpu_usage=server_result["cpu_usage"],
            disk_usage=server_result["disk_usage"],
            mem_usage=server_result["mem_usage"],
            when_created=str(datetime.datetime.now()).split(".")[0]
        ))
    return performance_list
