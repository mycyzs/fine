services = angular.module('webApiService', ['ngResource', 'utilServices']);

//生产代码
var POST = "POST";
var GET = "GET";

//测试代码
//var sourceRoute = "./Client/MockData";
//var fileType = ".html";
//var POST = "GET";
//var GET = "GET";
services.factory('sysService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            search_task_info: {method: POST, params: {actionName: 'search_task_info'}, isArray: false},
            get_host: {method: POST, params: {actionName: 'get_host'}, isArray: false},
            delete_task: {method: POST, params: {actionName: 'delete_task'}, isArray: false},
            search_host_list: {method: POST, params: {actionName: 'search_host_list'}, isArray: false},
            add_task: {method: POST, params: {actionName: 'add_task'}, isArray: false},
            modify_task: {method: POST, params: {actionName: 'modify_task'}, isArray: false},
            get_count_zhu: {method: POST, params: {actionName: 'get_count_zhu'}, isArray: false},
        });
}])


;//这是结束符，请勿删除