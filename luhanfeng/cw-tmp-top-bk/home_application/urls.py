# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^search_task_info$', 'search_task_info'),
    (r'^add_task$', 'add_task'),
    (r'^get_host$', 'get_host'),
    (r'^delete_task$', 'delete_task'),
    (r'^search_host_list$', 'search_host_list'),
    (r'^modify_task$', 'modify_task'),

)
