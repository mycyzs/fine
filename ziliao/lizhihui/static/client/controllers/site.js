controllers.controller("site", ["$scope", function ($scope) {
    var url = window.location.href.split("#/");
    $scope.pageUrl = "home";
    if (url.length !== 0) {
        $scope.pageUrl = url[1];
    }
    $scope.goToUrl = function (i) {
        $scope.pageUrl = i;
    }
}]);