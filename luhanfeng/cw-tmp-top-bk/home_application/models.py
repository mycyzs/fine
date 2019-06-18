# -*- coding: utf-8 -*-

from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=150, null=True)
    platform = models.CharField(max_length=30, null=True)
    execute_type = models.CharField(max_length=30, null=True)


class Host(models.Model):
    ip = models.CharField(max_length=50, null=True)
    life_time = models.CharField(max_length=50, null=True)
    cloud = models.CharField(max_length=30, null=True)
    host_id = models.IntegerField(null=True)
    biz_id = models.IntegerField(null=True)
    task_id = models.ForeignKey(Task)