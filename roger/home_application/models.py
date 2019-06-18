# -*- coding: utf-8 -*-

from django.db import models

class Server(models.Model):
    bk_host_innerip = models.CharField(max_length=40)
    bk_host_name = models.CharField(max_length=50)
    bk_cloud_id = models.CharField(max_length=30)
    bk_inst_name = models.CharField(max_length=50)
    bk_os_type = models.CharField(max_length=30)
    bk_biz_id = models.CharField(max_length=30)
    bk_biz_name = models.CharField(max_length=30)
    men = models.TextField(default='')
    disk = models.TextField(default='')
    creator = models.CharField(max_length=50,default='')

class monitor(models.Model):
    server=models.ForeignKey(Server)
    load = models.TextField()
    create_time = models.CharField(max_length=30,null=True,default='')