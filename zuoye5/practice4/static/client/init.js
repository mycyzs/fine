var app = angular.module("myApp", ['myController', 'utilServices', 'myDirective', 'ui.bootstrap', 'ui.router', 'webApiService','cwLeftMenu','ngGrid']);
var controllers = angular.module("myController", []);
var directives = angular.module("myDirective", []);


app.config(["$stateProvider", "$urlRouterProvider", "$httpProvider", function ($stateProvider, $urlRouterProvider, $httpProvider) {
    $httpProvider.defaults.headers.post['X-CSRFToken'] = $("#csrf").val();
    $urlRouterProvider.otherwise("/home");//默认展示页面
    $stateProvider.state('ListPage', {
        url: "/ListPage",
        controller: "ListPage",
        templateUrl: static_url + "client/views/ListPage.html"
    })
    .state('ReportPage', {
        url: "/ReportPage",
        controller: "ReportPage",
        templateUrl: static_url + "client/views/ReportPage.html"
    })
}]);


