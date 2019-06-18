# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^search_sys_info$', 'search_sys_info'),
    (r'^add_sys$', 'add_sys'),
    (r'^modify_sys$', 'modify_sys'),
    (r'^delete_sys$', 'delete_sys'),

)
