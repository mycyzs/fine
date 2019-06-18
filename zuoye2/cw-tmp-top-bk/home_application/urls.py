# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^api/test$', 'test'),
    (r'^search_sys_info$', 'search_sys_info'),
    (r'^add_order$', 'add_order'),
    (r'^modify_sys$', 'modify_sys'),
    (r'^delete_sys$', 'delete_sys'),
    (r'^agree$', 'agree'),
    (r'^refuse$', 'refuse'),
    (r'^get_count_obj$', 'get_count_obj'),
    (r'^get_count$', 'get_count'),
    (r'^search_order_info$', 'search_order_info'),
    (r'^get_all_user$', 'get_all_user'),

)
