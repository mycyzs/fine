controllers.controller("home", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal) {

    $scope.args = {
        order_name: "",
        checker: "",
        selected_id: "all"
    };

    //内容显示页数和数量
    $scope.PagingData = [];
    $scope.totalSerItems = 0;

    $scope.pagingOptions = {
        pageSizes: [10, 50, 100],
        pageSize: "10",
        currentPage: 1
    };
    $scope.template = [{id:'all',text:"所有"},{id:'created',text:"已创建"},{id:'submit',text:"已提交"},{id:'checking', text:'待审核'}];

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
    $scope.search_sys_info();


    $scope.$watch('pagingOptions', function (newVal, oldVal) {
        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
    }, true);


    $scope.add_sys = function () {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/addsys.html',
            windowClass: 'dialog_custom',
            controller: 'addSys',
            backdrop: 'static'
        });
        modalInstance.result.then(function (res) {
            $scope.hostList.unshift(res);
            $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
        })
    };

    $scope.modify_sys = function (row) {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/addsys.html',
            windowClass: 'dialog_custom',
            controller: 'modifySys',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return row.entity;
                }
            }
        });
        modalInstance.result.then(function (res) {
            row.entity.order_name = res.order_name;
            row.entity.checker = res.checker;
            row.entity.status = res.status;
            row.entity.content = res.content;
            row.entity.is_submit = res.is_submit;
        })
    };

    $scope.agree = function (row) {
        var id = row.entity.order_id;
        sysService.agree({}, {order_id: id}, function (res) {
                    if (res.result) {
                        $scope.hostList.splice(row.rowIndex, 1);
                        msgModal.open("success", "已审核，可在工单历史查看！");
                        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
                    }
                    else {
                        errorModal.open(res.msg);
                    }
                })
    };


    $scope.refuse = function (row) {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/my_test.html',
            windowClass: 'dialog_custom',
            controller: 'my_test',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return row.entity;
                }
            }
        });
        modalInstance.result.then(function (res) {
            $scope.hostList.splice(row.rowIndex, 1);
            $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
        })
    };


    $scope.delete_sys = function (row) {
        //根据id删除系统
        var id = row.entity.order_id;
        confirmModal.open({
            text: "确定删除该系统吗？",
            confirmClick: function () {
                loading.open();
                sysService.delete_sys({}, {order_id: id}, function (res) {
                    loading.close();
                    if (res.result) {
                        $scope.hostList.splice(row.rowIndex, 1);
                        msgModal.open("success", "删除工单成功！");
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
            {field: "order_name", displayName: "工单标题", width: 160},
            {field: "checker", displayName: "审核人", width: 140},
            {field: "status", displayName: "状态", width: 180},
            {field: "content", displayName: "工单内容", width: 500},
            {
                displayName: "操作",
                cellTemplate: '<div style="width:100%;padding-top:5px;text-align: center">' +
                '<span style="cursor: pointer" ng-if="row.entity.is_submit == \'false\'" class="btn btn-xs btn-primary" ng-click="modify_sys(row)">修改</span>&emsp;' +
                '<span style="cursor: pointer" ng-if="row.entity.is_deleted == \'true\'" class="btn btn-xs btn-danger" ng-click="delete_sys(row)">删除</span>&emsp;' +
                '<span style="cursor: pointer" ng-if="row.entity.is_checker == \'true\'" class="btn btn-xs btn-danger" ng-click="agree(row)">通过</span>&emsp;' +
                '<span style="cursor: pointer" ng-if="row.entity.is_checker == \'true\'" class="btn btn-xs btn-danger" ng-click="refuse(row)">拒绝</span>&emsp;' +
                '</div>'
            }
        ]
    };

}]);