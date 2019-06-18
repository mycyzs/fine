controllers.controller("home", function ($scope, sysService, loading, confirmModal, msgModal) {
    $scope.filterObj = {
        appID: "",
        ip: ""
    };
    $scope.appList = [];
    $scope.serverList = [];
    $scope.init = function () {
        loading.open();
        sysService.get_app_list({}, {}, function (res) {
            loading.close();
            $scope.appList = res.data;
        })
    };

    $scope.init();

    $scope.searchHost = function () {
        loading.open();
        sysService.search_server_by_filter({}, $scope.filterObj, function (res) {
            loading.close();
            if (res.result) {
                $scope.serverList = res.data;
            }
        })
    };


    $scope.gridOption = {
        data: 'serverList',
        columnDefs: [
            {field: 'ip_address', displayName: '内网IP'},
            {field: 'os_name', displayName: '系统名'},
            {field: 'host_name', displayName: '主机名'},
            {field: 'cloud_name', displayName: '云区域'},
            {field: 'mem_usage', displayName: 'Men（%）'},
            {field: 'disk_usage', displayName: 'Disk（%）'},
            {field: 'cpu_usage', displayName: 'CPU（%）'},
            {
                displayName: '操作', width: 180,
                cellTemplate: '<div style="width:100%;text-align: center;padding-top: 5px;">' +
                '<span class="fa fa-search fa-icon" ng-click="searchUsageInfo(row.entity)" title="查询"></span>&emsp;' +
                '<span ng-if="row.entity.is_add" class="fa fa-eye-slash fa-icon" ng-click="disable_get(row.entity)" title="移除"></span>' +
                '<span ng-if="!row.entity.is_add" class="fa fa-eye fa-icon" ng-click="enable_get(row.entity)" title="添加"></span>' +
                '</div>'
            }
        ]
    };

    $scope.searchUsageInfo = function (rowEntity) {
        confirmModal.open({
            text: "是否查询系统资源使用情况？",
            confirmClick: function () {
                loading.open();
                sysService.search_server_perform({}, rowEntity, function (res) {
                    loading.close();
                    if (res.result) {
                        rowEntity.mem_usage = res.data.mem_usage;
                        rowEntity.disk_usage = res.data.disk_usage;
                        rowEntity.cpu_usage = res.data.cpu_usage;
                    }
                })
            }
        })
    };

    $scope.enable_get = function (rowEntity) {
        confirmModal.open({
            text: '是否加入周期检查列表？',
            confirmClick: function () {
                loading.open();
                sysService.add_to_celery_list({}, rowEntity, function (res) {
                    loading.close();
                    if (res.result) {
                        msgModal.open("success", "添加成功");
                        rowEntity.is_add = true;
                    }
                })
            }
        })
    };
    $scope.disable_get = function (rowEntity) {
        confirmModal.open({
            text: '是否从周期检查列表移除？',
            confirmClick: function () {
                loading.open();
                sysService.remove_for_celery_list({}, rowEntity, function (res) {
                    loading.close();
                    if (res.result) {
                        msgModal.open("success", "移除成功");
                        rowEntity.is_add = false;
                    }
                })
            }
        })
    };
});
