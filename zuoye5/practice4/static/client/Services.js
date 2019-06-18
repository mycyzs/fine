services = angular.module('webApiService', ['ngResource', 'utilServices']);

var POST = "POST";
var GET = "GET";

services.factory('sysService', ['$resource', function ($resource) {
    return $resource(site_url + ':actionName/', {},
        {
            create_course: {method: POST, params: {actionName: 'create_course'}, isArray: false},
            search_biz: {method: POST, params: {actionName: 'search_biz'}, isArray: false},
            search_course_list: {method: POST, params: {actionName: 'search_course_list'}, isArray: false},
            get_all_course: {method: POST, params: {actionName: 'get_all_course'}, isArray: false},
            add_history: {method: POST, params: {actionName: 'add_history'}, isArray: false},
            search_report: {method: POST, params: {actionName: 'search_report'}, isArray: false},
            delete_course: {method: POST, params: {actionName: 'delete_course'}, isArray: false},

        });
}])


;//这是结束符，请勿删除