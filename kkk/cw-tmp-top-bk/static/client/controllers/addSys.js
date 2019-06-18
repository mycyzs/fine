controllers.controller("addSys", ["$scope", "loading", "$modalInstance", "msgModal", "sysService", "errorModal", "objectItem",function ($scope, loading, $modalInstance, msgModal, sysService, errorModal,objectItem) {
    $scope.title = "操作提示";
    $scope.args = {
        app_id: objectItem.app_id,
        set_id: objectItem.set_id,
        comment:''
    };
    $scope.userList=[];
    $scope.search_app = function () {
        loading.open();
        sysService.search_app({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.userList = res.data;
            } else {
                errorModal.open(res.msg);
            }
        })
    };
    //$scope.search_app();


    // $scope.dbOption1 = {
    //     data: "userList",
    //     multiple: false,
    //     modelData: ""
    // };


    $scope.hostList=[];
     $scope.changeDB = function () {
        loading.open();
        sysService.search_ip_by_app({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.hostList = res.data;
            } else {
                errorModal.open(res.msg);
            }
        })
    };

    //   $scope.dbOption2 = {
    //     data: "hostList",
    //     multiple: false,
    //     modelData: ""
    // };


    $scope.confirm = function () {


        //请求后台函数存入数据
        loading.open();
        sysService.add_sys({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                msgModal.open("success", "添加服务器成功！！");
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