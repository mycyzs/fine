controllers.controller("site", ["$scope",
function ($scope) {
    $scope.menuList = [
        {
            displayName: "任务列表", iconClass: "fa fa-tachometer fa-lg", url: "#/"
        },

    ];
    $scope.menuOption = {
        data: $scope.menuList
    };
}]);

