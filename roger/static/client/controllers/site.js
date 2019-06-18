controllers.controller("site", ["$scope", "sysService", "loading", "$timeout", function ($scope, sysService, loading, $timeout) {
    $scope.menuList = [
        {
            displayName: "首页", iconClass: "fa fa-cog fa-lg",url:'#/home',
        },

    ];


    $scope.menuOption = {
        data: 'menuList',
        locationPlaceHolder: '#locationPlaceHolder',
        adaptBodyHeight: CWApp.HeaderHeight + CWApp.FooterHeight
    };


}]);