controllers.controller("site", ["$scope", function ($scope) {
    $scope.menuList = [
        {
            displayName: "首页", iconClass: "fa fa-home", url: "#/home"
        },
        {
            displayName: "用户管理", iconClass: "fa fa-user ", children: [
                {
                    displayName: "页面1", iconClass:"fa fa-home", url: "#/mail"
                }, {
                    displayName: "页面2", url: "#/log"
                }
            ]
        },
        {
            displayName: "自定义", iconClass: "fa fa-user ", children: [
                {
                    displayName: "自定义页面1", iconClass:"fa fa-home", url: "#/mail"
                }
            ]
        }
    ];

    $scope.menuOption = {
        data: 'menuList',
        locationPlaceHolder: '#locationPlaceHolder',
        adaptBodyHeight: CWApp.HeaderHeight + CWApp.FooterHeight
    };

}]);