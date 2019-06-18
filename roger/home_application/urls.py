# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    # 首页--your index
    (r'^$', 'home'),
    (r'^api/test', 'test'),
    (r'^get_server_list$', 'get_server_list'),
    (r'^get_biz_list$', 'get_biz_list'),
    (r'^get_server_by_biz$', 'get_server_by_biz'),
    (r'^add_server$', 'add_server'),
    (r'^del_server$', 'del_server'),
    (r'^get_server_monitor$', 'get_server_monitor'),

)
