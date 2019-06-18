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
            search_sys_info: {method: POST, params: {actionName: 'search_sys_info'}, isArray: false},
            add_order: {method: POST, params: {actionName: 'add_order'}, isArray: false},
            modify_sys: {method: POST, params: {actionName: 'modify_sys'}, isArray: false},
            delete_sys: {method: POST, params: {actionName: 'delete_sys'}, isArray: false},
            agree: {method: POST, params: {actionName: 'agree'}, isArray: false},
            refuse: {method: POST, params: {actionName: 'refuse'}, isArray: false},
            get_count_obj: {method: POST, params: {actionName: 'get_count_obj'}, isArray: false},
            get_count: {method: POST, params: {actionName: 'get_count'}, isArray: false},
            get_count_zhu: {method: POST, params: {actionName: 'get_count_zhu'}, isArray: false},
            search_order_info: {method: POST, params: {actionName: 'search_order_info'}, isArray: false},
            get_all_user: {method: POST, params: {actionName: 'get_all_user'}, isArray: false},
        });
}])


;//这是结束符，请勿删除