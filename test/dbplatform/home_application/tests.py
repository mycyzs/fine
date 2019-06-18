# -*- coding: utf-8 -*-

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

# import from apps here


# import from lib
from django.test import TestCase
from django.db import models
from home_application.models import QSInfo,LVSInfo

lvsinfo=QSInfo.objects.filter(role__exact='QS').values('lvsinfo_id').distinct()

print(lvsinfo)










