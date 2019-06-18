var app = angular.module("myApp", ['myController', 'utilServices', 'myDirective', 'ui.bootstrap', 'ui.router', 'webApiService', 'cwLeftMenu', 'ngGrid']);
var controllers = angular.module("myController", []);
var directives = angular.module("myDirective", []);


app.config(["$stateProvider", "$urlRouterProvider", "$httpProvider", function ($stateProvider, $urlRouterProvider, $httpProvider) {
    $httpProvider.defaults.headers.post['X-CSRFToken'] = $("#csrf").val();
    $urlRouterProvider.otherwise("/home");//默认展示页面
    $stateProvider.state('home', {
        url: "/home",
        controller: "home",
        templateUrl: static_url + "client/views/home.html"
    })
        .state('add_task', {
            url: "/add_task",
            controller: "add_task",
            templateUrl: static_url + "client/views/add_task.html"
        })
        .state('modify_task', {
            url: "/modify_task?task_id",
            controller: "modify_task",
            templateUrl: static_url + "client/views/add_task.html"
        })

        .state('zhu_test', {
            url: "/zhu_test",
            controller: "zhu_test",
            templateUrl: static_url + "client/views/sysconfig.html"
        })

        .state('host_list', {
            url: "/host_list?task_id",
            controller: "host_list",
            templateUrl: static_url + "client/views/host_list.html"
        })


}]);
