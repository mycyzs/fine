controllers.controller("modifySys", ["$scope","loading","$modalInstance","msgModal","objectItem","sysService","errorModal",function ( $scope,loading,$modalInstance,msgModal,objectItem,sysService,errorModal) {
    $scope.title = "修改备注信息";
    $scope.args = {
        id:objectItem.id,
        comment:objectItem.comment,
        app_id:objectItem.app_id,
        server_ip:objectItem.server_ip
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
    $scope.search_app();

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
       $scope.changeDB()

    // $scope.dbOption1 = {
    //     data: "userList",
    //     multiple: false,
    //     modelData: ""
    // };


    $scope.confirm = function () {
        // if ($scope.args.sys_name == '') {
        //     msgModal.open("error", "请输入系统名！");
        //     return
        // }


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
     $scope.get_count_obj = function () {
        loading.open();
        sysService.get_count_obj({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.data_list = res.data

            } else {
                errorModal.open(res.message);
            }
        });
    };
    $scope.get_count_obj();


    // 饼图
    $scope.mysql_pie = {
        data: "data_list",
        title: {text: 'MySQL版本占比', enabled: true},
        unit: "",
        size: "200px"
    };






    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    };








}]);