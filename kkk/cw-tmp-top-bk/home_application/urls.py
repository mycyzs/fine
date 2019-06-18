# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^t/luhanfeng-1901/api/test/$', 'test'),
    (r'^search_ip_info$', 'search_host'),
    (r'^add_sys$', 'get_job_by_id'),
    (r'^modify_sys$', 'modify_sys'),
    (r'^delete_sys$', 'delete_sys'),
    (r'^search_init$', 'search_app_host'),
    (r'^get_count_obj$', 'get_count_obj'),
    (r'^get_count$', 'get_count'),
    (r'^get_count_zhu$', 'get_count_zhu'),
    (r'^search_app$', 'search_app'),
    (r'^search_ip_by_app$', 'search_set'),
    (r'^search_info$', 'search_info'),
    (r'^search_load$', 'search_load'),
    (r'^search_hosts$', 'search_hosts'),

)
