controllers.controller("home", ["msgModal", "$scope", "loading", "sysService", "$modal","confirmModal", function (msgModal, $scope, loading, sysService, $modal,confirmModal) {
    $scope.filterObj = {
        name: ''
    };
    $scope.search = function () {
        loading.open();
        sysService.get_server_list({}, $scope.filterObj, function (res) {
            loading.close();
            if (res.result) {
                $scope.table_data = res.data
            } else {
                msgModal.open('error', '获取数据失败，请联系管理员！')
            }
        })
    };
    $scope.search();
    $scope.table_data = [];
    $scope.table_option = {
        bottom: 30,
        data: 'table_data',
        title: [
            {title: '主机ip', rgwidth: '20%', enname: 'bk_host_innerip'},
            {title: '主机名称', rgwidth: '20%', enname: 'bk_host_name'},
            {title: '所属业务', rgwidth: '20%', enname: 'bk_biz_name'},
            {title: '操作系统类型', rgwidth: '20%', enname: 'bk_os_type'},
            {
                title: '操作', rgwidth: '20%', rghtml: '<div>' +
            '<button style="margin: 0 3px" class="btn btn-sm btn-info" ui-sref="monitor({id:i.id})">查看性能</button>' +
            '<button style="margin: 0 3px" class="btn btn-sm btn-danger" ng-click="del(i.id)">删除</button>' +
            '</div>'
            },
        ]
    };
    $scope.add = function () {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/test/add_ip.html',
            windowClass: 'add_ip',
            controller: 'add_ip',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return ''
                }
            }
        });
        modalInstance.result.then(function (res) {
            $scope.search()
        })
    };
    $scope.del = function (id) {
        confirmModal.open({
            text: "是否要删除？",
            confirmClick: function () {
                loading.open();
                sysService.del_server({}, {id: id}, function (res) {
                    loading.close();
                    if (res.result) {
                        $scope.search();
                        msgModal.open('success', '删除成功！')
                    } else {
                        msgModal.open('error', '删除数据失败，请联系管理员！')
                    }
                })
            }
        })

    }
}]);
