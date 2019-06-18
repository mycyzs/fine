controllers.controller("detail", ["$scope","loading","$modalInstance","msgModal","objectItem","sysService","errorModal",function ( $scope,loading,$modalInstance,msgModal,objectItem,sysService,errorModal) {
    $scope.title = "课程信息";
    $scope.site_u = site_url;
    $scope.now_id = objectItem.id;
    $scope.current_url = window.location.href.split('#')[0];
    $scope.args = {
        id:objectItem.id,
        name: objectItem.name,
        content: objectItem.content,
        comment:objectItem.comment,
        biz: objectItem.biz
    };

    $scope.userList = []
    $scope.inits = function () {
        loading.open();
        sysService.search_biz({}, {}, function (res) {
            loading.close();
            $scope.userList = res.data
        })
    };
    $scope.inits();


    $scope.init_sum = function(){
        sysService.init_sum({}, {id: $scope.args.id}, function (res) {
            loading.close();

        })
    }
    $scope.init_sum();
    $scope.dbOption1 = {
        data: "userList",
        multiple: false,
        modelData: "args.biz"
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
         sysService.modify_sys({}, $scope.args, function (res) {
             loading.close();
             if (res.result) {
                 msgModal.open("success", "修改成功！！");
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