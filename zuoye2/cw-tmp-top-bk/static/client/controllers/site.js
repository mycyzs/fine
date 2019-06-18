controllers.controller("site", ["$scope",
function ($scope) {
    $scope.menuList = [
        {
            displayName: "工单管理", iconClass: "fa fa-tachometer fa-lg", url: "#/"
        },
        {displayName: "历史工单", url: "#/orderHistory"},


    ];
    $scope.menuOption = {
        data: $scope.menuList
    };
}]);

