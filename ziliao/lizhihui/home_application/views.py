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
from blueking.component.shortcuts import get_client_by_request
from home_application.celery_tasks import *
import datetime


def test(request):
    return render_json({"result": True, "message": "success", "data": request.user.username})


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def get_app_list(request):
    client = get_client_by_request(request)
    result = get_business_by_user(client, request.user.username)
    return render_json(result)


def search_server_by_filter(request):
    filter_obj = json.loads(request.body)
    client = get_client_by_request(request)
    result = search_host(client, filter_obj,request.user.username)
    if not result["result"]:
        return render_json({"result": False, "data": []})
    return_data = []
    for i in result["data"]["info"]:
        if i["host"]["bk_os_type"] != "1":
            continue
        one_obj = {
            "ip_address": i["host"]["bk_host_innerip"],
            "host_name": i["host"]["bk_host_name"],
            "os_name": i["host"]["bk_os_name"],
            "cloud_name": i["host"]["bk_cloud_id"][0]["bk_inst_name"],
            "cloud_id": i["host"]["bk_cloud_id"][0]["bk_inst_id"],
            "app_id": i["biz"][0]["bk_biz_id"],
            "cpu_usage": "--",
            "mem_usage": "--",
            "disk_usage": "--",
        }
        one_obj["is_add"] = Servers.objects.filter(app_id=one_obj["app_id"], ip_address=one_obj["ip_address"], cloud_id=one_obj["cloud_id"], is_deleted=False).exists()
        return_data.append(one_obj)
    return render_json({"result": True, "data": return_data})


def search_host(client, filter_obj,username):
    kwargs = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
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
                        "value": filter_obj["appID"]
                    }
                ]
            }
        ]
    }
    if filter_obj["ip"].strip():
        kwargs["ip"] = {
            "flag": "bk_host_innerip|bk_host_outerip",
            "exact": 1,
            "data": filter_obj["ip"].strip().split("\n")
        }
    result = client.cc.search_host(kwargs)
    return result


def search_server_perform(request):
    server_obj = json.loads(request.body)
    client = get_client_by_request(request)
    check_app = {
        "app_id": server_obj["app_id"],
        "ip_list": [{"ip": server_obj["ip_address"], "bk_cloud_id": server_obj["cloud_id"]}],
    }
    result = get_server_perform(client, check_app, request.user.username)
    if result["result"]:
        script_result = get_task_ip_log(client, check_app["app_id"], result["data"], request.user.username)
        if script_result:
            return_data = format_log_content(script_result[0]["log_content"])
            result["data"] = return_data
    return render_json(result)


def add_to_celery_list(request):
    server_obj = json.loads(request.body)
    Servers.objects.update_or_create(
        ip_address=server_obj["ip_address"],
        cloud_id=server_obj["cloud_id"],
        app_id=server_obj["app_id"],
        os_name=server_obj["os_name"],
        cloud_name=server_obj["cloud_name"], defaults={
            "is_deleted": False,
            "created_by": request.user.username

        }
    )
    return render_json({"result": True})


def remove_for_celery_list(request):
    server_obj = json.loads(request.body)
    Servers.objects.filter(
        ip_address=server_obj["ip_address"],
        cloud_id=server_obj["cloud_id"],
        app_id=server_obj["app_id"]
    ).update(is_deleted=True)
    return render_json({"result": True})


def search_server_perform_list(request):
    filter_obj = json.loads(request.body)
    if filter_obj["appID"] == "":
        servers = Servers.objects.filter(is_deleted=False)
    else:
        servers = Servers.objects.filter(app_id=filter_obj["appID"],is_deleted=False)
    if filter_obj["ip"].strip():
        ip_list = filter_obj["ip"].split("\n")
        servers = servers.filter(ip_address__in=ip_list,is_deleted=False)
    return_data = []
    perform_obj = {}
    for i in servers:
        key = i.ip_address.replace(".", "_")
        result = get_one_server_line_chart_data(i)
        one_obj = {
            "ip_address": i.ip_address,
            "name": 'performObj.ip%s' % key,
            "categories": result['categories']
        }
        return_data.append(one_obj)
        perform_obj["ip" + key] = result["data"]
    return render_json({"result": True, "data": return_data, "perform_obj": perform_obj})


def get_one_server_line_chart_data(i={}):
    date_now = datetime.datetime.now() + datetime.timedelta(hours=-1)

    server_performs = ServerPerformance.objects.filter(server_id=i.id, when_created__gt=str(date_now).split(".")[0]).order_by("id")
    one_obj = [
        {"name": "cpu", "data": [i.cpu_usage for i in server_performs]},
        {"name": "mem", "data": [i.mem_usage for i in server_performs]},
        {"name": "disk", "data": [i.disk_usage for i in server_performs]},
    ]
    return {"categories": [i.when_created for i in server_performs], "data": one_obj}
