/**
 * Created by Roger on 2019/1/3.
 */
controllers.controller('add_ip', ["$scope", "sysService", "msgModal", "$modalInstance", "loading", "errorModal","objectItem", function ($scope, sysService, msgModal, $modalInstance, loading, errorModal,objectItem) {
    $scope.biz_list = [];
    $scope.up_data = {
        'bk_biz_id':'',
        'bk_host_innerip':''
    };
    $scope.search_biz = function () {
        loading.open();
        sysService.get_biz_list({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.biz_list = res.data;
                $scope.up_data.bk_biz_id = res.data[0]['bk_biz_id']+'';
                $scope.choose($scope.up_data.bk_biz_id)
            } else {
                msgModal.open('error', '获取数据失败，请联系管理员！')
            }
        })
    };
    $scope.search_biz();
    $scope.ip_list = [];
    $scope.choose = function (biz) {
        loading.open();
        sysService.get_server_by_biz({}, {id:biz}, function (res) {
            loading.close();
            if (res.result) {
                $scope.ip_list = res.data
            } else {
                msgModal.open('error', '获取数据失败，请联系管理员！')
            }
        })
    };

    $scope.confirm = function () {
        loading.open();
        sysService.add_server({}, $scope.up_data, function (res) {
            loading.close();
            if (res.result) {
                $modalInstance.close();
            } else {
                errorModal.open([res['error']])
            }
        })
    };

    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    };
}]);