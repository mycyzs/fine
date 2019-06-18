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
            get_server_list: {method: POST, params: {actionName: 'get_server_list'}, isArray: false},
            get_biz_list: {method: POST, params: {actionName: 'get_biz_list'}, isArray: false},
            get_server_by_biz: {method: POST, params: {actionName: 'get_server_by_biz'}, isArray: false},
            add_server: {method: POST, params: {actionName: 'add_server'}, isArray: false},
            del_server: {method: POST, params: {actionName: 'del_server'}, isArray: false},
            get_server_monitor: {method: POST, params: {actionName: 'get_server_monitor'}, isArray: false},
        });
}])
;//这是结束符，请勿删除