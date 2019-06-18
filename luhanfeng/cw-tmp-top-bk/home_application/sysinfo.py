# -*- coding:utf-8 -*-
import json

from blueking.component.shortcuts import get_client_by_request
from common.log import logger
from common.mymako import render_json
from home_application.models import Task, Host


def search_task_info(request):
    try:
        username = request.user.username
        request_data = json.loads(request.body)
        if request_data["selected_id"] == "all":
            request_data["selected_id"] = ''
        tasks = Task.objects.filter(name__icontains=request_data["task_name"], email__icontains=request_data["email"],
                                    execute_type__icontains=request_data["selected_id"], platform__icontains=request_data["platform"])
        return_data = []
        for task in tasks:
            return_data.append(
                {
                    "task_id": task.id,
                    "task_name": task.name,
                    "execute_type": u"立即执行" if task.execute_type == 'now' else u"定时",
                    "email": task.email,
                    "platform": task.platform
                }
            )
        return render_json({"result": True, "data": return_data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询任务信息失败!!"]})


def add_task(request):
    try:
        request_data = json.loads(request.body)
        task_data = {
            "name": request_data["task_name"],
            "execute_type": request_data["execute_type"],
            "email": request_data["email"],
            "platform": request_data["platform"]
        }
        host_data = request_data["ip_list"]
        task = Task.objects.create(**task_data)
        for host in host_data:
            host["host_id"] = host["id"]
            del host["id"]
            Host.objects.create(task_id=task, **host)
        return render_json({"result": True})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"添加任务信息失败!!"]})


def get_host(request):
    try:
        request_data = json.loads(request.body)
        task = Task.objects.get(id=request_data["task_id"])
        hosts = Host.objects.filter(task_id=task)
        return_data = []
        host_info = {
            "host_id": [],
            "task_name": task.name,
            "execute_type": task.execute_type,
            "platform": task.platform,
            "email": task.email
        }
        for host in hosts:
            return_data.append({
                "id": host.host_id,
                "ip": host.ip,
                "life_time": host.life_time,
                "cloud": host.cloud,
                "biz_id": host.biz_id
            })
            host_info["host_id"].append(str(host.host_id))
        return render_json({"result": True, "data": return_data, "host_info": host_info})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"获取任务信息失败!!"]})


def delete_task(request):
    try:
        request_data = json.loads(request.body)
        task = Task.objects.get(id=request_data["task_id"])
        Host.objects.filter(task_id=task).delete()
        task.delete()
        return render_json({"result": True})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"删除任务失败!!"]})


def modify_task(request):
    try:
        request_data = json.loads(request.body)
        task_data = {
            "name": request_data["task_name"],
            "execute_type": request_data["execute_type"],
            "email": request_data["email"],
            "platform": request_data["platform"]
        }
        Task.objects.filter(id=request_data["task_id"]).update(**task_data)
        task = Task.objects.get(id=request_data["task_id"])
        Host.objects.filter(task_id=task).delete()
        host_data = request_data["ip_list"]
        for host in host_data:
            host["host_id"] = host["id"]
            del host["id"]
            Host.objects.create(task_id=task, **host)
        return render_json({"result": True})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"修改任务信息失败!!"]})


def search_host_list(request):
    try:
        request_data = json.loads(request.body)
        task = Task.objects.get(id=request_data["task_id"])
        hosts = Host.objects.filter(task_id=task)
        return_data = []
        for host in hosts:
            return_data.append(
                {
                    "ip": host.ip,
                    "life_time": host.life_time,
                    "cloud": host.cloud,
                }
            )
        return render_json({"result": True, "data": return_data})
    except Exception as e:
        logger.error(e)
        return render_json({"result": False, "msg": [u"查询主机信息失败!!"]})