controllers.controller("site", ["$scope",
function ($scope) {
    $scope.menuList = [
        {
            displayName: "首页", iconClass: "fa fa-tachometer fa-lg", url: "#/"
        },
        {displayName: "访客量", url: "#/test"},

    ];
    $scope.menuOption = {
        data: $scope.menuList
    };
}]);

