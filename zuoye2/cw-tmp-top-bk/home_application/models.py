# -*- coding: utf-8 -*-

from django.db import models


class Order(models.Model):
    STATUS = {"created": u"已创建", "submit": u"已提交", "checking": u"待审核", "checked": u"已审核"}

    order_name = models.CharField(max_length=30, null=False)
    creator = models.CharField(max_length=30, null=True)
    checker = models.CharField(max_length=30, null=False)
    content = models.TextField(null=True)
    status = models.CharField(max_length=30, null=False)

    def get_status(self):

        return self.STATUS.get(self.status)


class OrderList(models.Model):
    STATUS = {'agree': u'通过', 'refuse': u'拒绝'}

    check_status = models.CharField(max_length=30, null=False)
    comment = models.TextField(null=True)
    order = models.ForeignKey(Order)

    def get_check_status(self):

        return self.STATUS.get(self.check_status)