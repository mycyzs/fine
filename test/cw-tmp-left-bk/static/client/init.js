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
    $stateProvider.state('mail', {
        url: "/mail",
        controller: "mail",
        templateUrl: static_url + "client/views/mail.html"
    })
    $stateProvider.state('log', {
        url: "/log",
        controller: "log",
        templateUrl: static_url + "client/views/log.html"
    })







}]);
