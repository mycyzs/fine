# -*- coding: utf-8 -*-

from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=30, null=True)
    content = models.TextField(null=True)
    comment = models.TextField(null=True)
    biz = models.CharField(max_length=30, null=True)
    creator = models.CharField(max_length=30, null=True)
    when_created = models.CharField(max_length=50, null=True)
    background_img = models.BinaryField(null=True)


class Total(models.Model):
    book = models.ForeignKey(Book)
    date = models.CharField(max_length=50, null=True)
    sum = models.IntegerField(null=True)
