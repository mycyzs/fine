services = angular.module('webApiService', ['ngResource', 'utilServices']);

var POST = "POST";
var GET = "GET";

services.factory('sysService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            get_app_list: {method: POST, params: {actionName: 'get_app_list'}, isArray: false},
            search_server_by_filter: {method: POST, params: {actionName: 'search_server_by_filter'}, isArray: false},
            search_server_perform: {method: POST, params: {actionName: 'search_server_perform'}, isArray: false},
            add_to_celery_list: {method: POST, params: {actionName: 'add_to_celery_list'}, isArray: false},
            remove_for_celery_list: {method: POST, params: {actionName: 'remove_for_celery_list'}, isArray: false},
            search_server_perform_list: {method: POST, params: {actionName: 'search_server_perform_list'}, isArray: false},
        });
}])


;//这是结束符，请勿删除