controllers.controller("my_test", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", "$stateParams", "objectItem","$modalInstance", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal, $stateParams, objectItem,$modalInstance) {
    $scope.title = "审核拒绝";

    $scope.args = {
        comment: '',
        order_id: objectItem.order_id
    }


    $scope.commit = function () {

        if ($scope.args.comment == '') {
            msgModal.open("error", "请填写拒绝理由！");
            return
        }
        sysService.refuse({}, $scope.args, function (res) {
            if (res.result) {
                msgModal.open("success", "已审核，可在工单历史查看！");
                $modalInstance.close(res.data);
            }
            else {
                errorModal.open(res.msg);
            }
        })
    };


    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    };

}]);


