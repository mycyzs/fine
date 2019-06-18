# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'home'),
    (r'^api/test$', 'test'),
    (r'^get_app_list$', 'get_app_list'),
    (r'^search_server_by_filter$', 'search_server_by_filter'),
    (r'^search_server_perform$', 'search_server_perform'),
    (r'^add_to_celery_list$', 'add_to_celery_list'),
    (r'^remove_for_celery_list$', 'remove_for_celery_list'),
    (r'^search_server_perform_list$', 'search_server_perform_list'),


)
