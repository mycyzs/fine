# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^search_sys_info$', 'search_sys_info'),
    (r'^add_sys$', 'add_sys'),
    (r'^modify_sys$', 'modify_sys'),
    (r'^delete_sys$', 'delete_sys'),
    (r'^search_init$', 'search_inst_detail'),
    (r'^get_count_obj$', 'get_count_obj'),
    (r'^get_count$', 'get_count'),
    (r'^get_count_zhu$', 'get_count_zhu'),

)
