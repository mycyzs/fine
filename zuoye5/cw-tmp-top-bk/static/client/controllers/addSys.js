controllers.controller("addSys", ["$scope","loading","$modalInstance","msgModal","sysService","errorModal",function ( $scope,loading,$modalInstance,msgModal,sysService,errorModal) {
    $scope.title = "添加系统";
    $scope.args = {
        name: "",
        content: "",
        biz:"",
        comment:""
    };
    $scope.userList = [];

    // 获取所有业务
    $scope.inits = function () {
        loading.open();
        sysService.search_biz({}, {}, function (res) {
            loading.close();
            $scope.userList = res.data
        })
    };
    $scope.inits();

    $scope.dbOption1 = {
        data: "userList",
        multiple: false,
        modelData: ""
    };

    $scope.confirm = function () {
        if ($scope.args.name == '') {
            msgModal.open("error", "请输入课程名！");
            return
        }
         if ($scope.args.content == '') {
            msgModal.open("error", "请输入内容！");
            return
        }
         if ($scope.args.comment == '') {
            msgModal.open("error", "请输入备注！");
            return
        }
         if ($scope.args.biz == '') {
            msgModal.open("error", "请选择业务！");
            return
        }

        //请求后台函数存入数据
        loading.open();
        sysService.add_sys({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                msgModal.open("success", "添加课程成功！！");
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