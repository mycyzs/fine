controllers.controller("my_test", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", "$stateParams",function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal,$stateParams) {
    $scope.inits = function () {
        loading.open();
        sysService.search_init({}, $scope.args, function (res) {
            loading.close();

        })
    };
    $scope.inits();

}]);


