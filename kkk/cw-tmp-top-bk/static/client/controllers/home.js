controllers.controller("home", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal) {

    $scope.args = {
        app_id: "",
        set_id: '',
        server_ip: "",
        comment: ''
    };

    $scope.userList = [];
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

    $scope.setList = [];
    $scope.changeDB = function () {
        loading.open();
        sysService.search_ip_by_app({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.setList = res.data;
            } else {
                errorModal.open(res.msg);
            }
        })
    };


    //内容显示页数和数量
    $scope.PagingData = [];
    $scope.totalSerItems = 0;

    $scope.pagingOptions = {
        pageSizes: [10, 50, 100],
        pageSize: "10",
        currentPage: 1
    };
    $scope.template = [{id: 1, text: "aaa"}, {id: 2, text: "bbb"}];

    $scope.templateOption = {
        data: "template",
        multiple: false,
    };


    $scope.setPagingData = function (data, pageSize, page) {
        $scope.PagingData = data.slice((page - 1) * pageSize, page * pageSize);
        $scope.totalSerItems = data.length;
        if (!$scope.$$phase) {
            $scope.$apply();
        }
    };

    $scope.getPagedDataAsync = function (pageSize, page) {
        $scope.setPagingData($scope.hostList ? $scope.hostList : [], pageSize, page);
    };


    $scope.changeDB1 = function () {
        loading.open();
        sysService.search_hosts({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.hostList = res.data;
                $scope.pagingOptions.currentPage = 1;
                $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
            } else {
                errorModal.open(res.msg);
            }
        })
    };


    //查询系统表
    $scope.search_sys_info = function () {
        loading.open();
        sysService.search_sys_info({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.hostList = res.data;
                $scope.pagingOptions.currentPage = 1;
                $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
            } else {
                errorModal.open(res.msg);
            }
        })
    };
    // $scope.search_sys_info();


    $scope.$watch('pagingOptions', function (newVal, oldVal) {
        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
    }, true);


    $scope.add_sys = function () {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/addsys.html',
            windowClass: 'dialog_custom',
            controller: 'addSys',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return {
                        app_id: $scope.args.app_id,
                        set_id:$scope.args.set_id
                    };
                }
            }
        });
        modalInstance.result.then(function (res) {

        })
    };

    $scope.modify_sys = function (row) {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/modify.html',
            windowClass: 'dialog_custom',
            controller: 'modifySys',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return {
                        id: row.entity.id,
                        comment: row.entity.comment,
                        app_id: row.entity.app_id,
                        server_ip: row.entity.host_ip
                    };
                }
            }
        });
        modalInstance.result.then(function (res) {
            row.entity.comment = res.comment;

        })
    };


    $scope.delete_sys = function (row) {
        //根据id删除系统
        var id = row.entity.id;
        confirmModal.open({
            text: "确定删除该服务器吗？",
            confirmClick: function () {
                loading.open();
                sysService.delete_sys({}, {id: id}, function (res) {
                    loading.close();
                    if (res.result) {
                        $scope.hostList.splice(row.rowIndex, 1);
                        msgModal.open("success", "删除系统成功！");
                        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
                    }
                    else {
                        errorModal.open(res.message);
                    }
                })
            }
        });

    };


    $scope.gridOption = {
        data: "PagingData",
        enablePaging: true,
        enableColumnResize: true,
        showFooter: true,
        pagingOptions: $scope.pagingOptions,
        totalServerItems: 'totalSerItems',
        columnDefs: [
            {field: "host_ip", displayName: "内网ip", width: 200},
            {field: "bk_os_name", displayName: "系统名", width: 170},
            {field: "host_name", displayName: "主机名", width: 150},
            {field: "bk_cloud_name", displayName: "云区域", width: 160},
            {field: "os_type", displayName: "操作类型", width: 130},
            {
                displayName: "操作",
                cellTemplate: '<div style="width:100%;padding-top:5px;text-align: center">' +
                '<span style="cursor: pointer" class="btn btn-xs btn-primary" ui-sref="check_s({host_id:row.entity.id})">查看性能</span>&emsp;' +
                '<span style="cursor: pointer" class="btn btn-xs btn-danger" ng-click="delete_sys(row)">删除</span>' +
                '<span style="cursor: pointer;margin-left: 10px" class="btn btn-xs btn-danger" ng-click="modify_sys(row)">修改</span>' +
                '</div>'
            }
        ]
    };

}]);