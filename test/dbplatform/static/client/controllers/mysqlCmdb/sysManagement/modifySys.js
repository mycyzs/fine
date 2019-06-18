controllers.controller("modifySys", ["$scope","loading","$modalInstance","msgModal","objectItem","sysService","errorModal",function ( $scope,loading,$modalInstance,msgModal,objectItem,sysService,errorModal) {
    $scope.title = "修改系统信息";
    $scope.args = {
        id:objectItem.id,
        sys_name: objectItem.sys_name,
        sys_code: objectItem.sys_code,
        first_owner:objectItem.first_owner,
        is_control:(objectItem.is_control == "否")? is_control="0": is_control="1"
    };

    $scope.userList = [{id:"cyz", text:"cyz"},{id:"lhf",text:"lhf"}];
    $scope.dbOption1 = {
        data: "userList",
        multiple: false,
        modelData: "args.first_owner"
    };
    $scope.dbOption2 = {
        data: "userList",
        multiple: false,
        modelData: "args.second_owner"
    };
    $scope.dbOption3 = {
        data: "userList",
        multiple: false,
        modelData: "args.third_owner"
    };

    $scope.confirm = function () {
        var args = angular.copy($scope.args);
        if (args.sys_name == '') {
            msgModal.open("error", "请输入系统名！");
            return
        }
        if (args.sys_code == '') {
            msgModal.open("error", "请输入系统简称！");
            return
        }
        if (args.first_owner == '') {
            msgModal.open("error", "请输入第一负责人！");
            return
        }
        if (args.is_control  == "") {
            msgModal.open("error", "请选择权限控制");
            return;
        }
        if (args.department  == "") {
            msgModal.open("error", "请输入所属产品线");
            return;
        }
        if (args.db_type  == "") {
            msgModal.open("error", "请输入类型");
            return;
        }

        //请求后台函数存入数据
         loading.open();
         sysService.modify_sys({}, $scope.args, function (res) {
             loading.close();
             if (res.result) {
                 msgModal.open("success", "修改成功！！");
                 $modalInstance.close(res.data);
             }
             else {
                 errorModal.open(res.message);
             }
         })
    };

    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    };








}]);