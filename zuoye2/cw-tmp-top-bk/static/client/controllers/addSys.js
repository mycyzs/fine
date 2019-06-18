controllers.controller("addSys", ["$scope","loading","$modalInstance","msgModal","sysService","errorModal",function ( $scope,loading,$modalInstance,msgModal,sysService,errorModal) {
    $scope.title = "添加系统";
    $scope.args = {
        order_name: "",
        check_owner:"",
        content:""
    };
    $scope.userList = [];

    $scope.dbOption1 = {
        data: "userList",
        multiple: false,
        modelData: ""
    };


    // 获取平台所有用户
    $scope.get_all_user = function(){
        sysService.get_all_user({}, {}, function (res) {
            if (res.result) {
                $scope.userList = res.data
             }
            else {
                errorModal.open(res.msg);
             }
         })
    };

    $scope.get_all_user();

    $scope.save = function () {
        $scope.args.status = 'created';
        if ($scope.args.order_name == '') {
            msgModal.open("error", "请输入工单标题！");
            return
        }
        if ($scope.args.check_owner == '') {
            msgModal.open("error", "请选择审批人！");
            return
        }
        if ($scope.args.content == '') {
            msgModal.open("error", "请填写工单内容！");
            return
        }
        //请求后台函数存入数据
        loading.open();
        sysService.add_order({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                msgModal.open("success", "新增工单成功！！");
                $modalInstance.close(res.data);
             }
            else {
                errorModal.open(res.msg);
             }
         })
    };

    $scope.submit = function () {
        $scope.args.status = 'submit';
        if ($scope.args.order_name == '') {
            msgModal.open("error", "请输入工单标题！");
            return
        }
        if ($scope.args.check_owner == '') {
            msgModal.open("error", "请选择审批人！");
            return
        }
        if ($scope.args.content == '') {
            msgModal.open("error", "请填写工单内容！");
            return
        }
        //请求后台函数存入数据
        loading.open();
        sysService.add_order({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                msgModal.open("success", "新增工单成功！！");
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