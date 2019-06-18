# -*- coding: utf-8 -*-

from django.db import models


class Host(models.Model):
    host_ip = models.CharField(max_length=30)
    host_name = models.CharField(max_length=30,null=True)
    app_name = models.CharField(max_length=20)
    app_id = models.CharField(max_length=20)
    cloud_name = models.CharField(max_length=20)
    cloud_id = models.CharField(max_length=20)
    os_type = models.CharField(max_length=20,null=True)
    disk = models.TextField(default='')
    men = models.TextField(default='')
    comment = models.CharField(max_length=300,null=True)
    # is_success = models.BooleanField(default=False)
    # text = models.TextField(null=True)
    # when_created = models.CharField(max_length=50,null=True)


class Load(models.Model):
    load_info = models.TextField(default='')
    created_time = models.CharField(max_length=60,default='',null=True)
    host = models.ForeignKey(Host)