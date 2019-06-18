var app = angular.module("myApp", ['myController', 'utilServices', 'myDirective', 'ui.bootstrap', 'ui.router', 'webApiService','cwLeftMenu','ngGrid']);
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
    .state('hostInfo', {
        url: "/hostInfo",
        controller: "hostInfo",
        templateUrl: static_url + "client/views/hostInfo.html"
    })

}]);


