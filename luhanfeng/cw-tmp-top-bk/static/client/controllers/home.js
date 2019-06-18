controllers.controller("home", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal","$state", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal,$state) {

    $scope.args = {
        task_name: "",
        email: "",
        platform: "",
        selected_id: ""
    };
    $scope.taskList = [];

    //内容显示页数和数量
    $scope.PagingData = [];
    $scope.totalSerItems = 0;

    $scope.pagingOptions = {
        pageSizes: [10, 50, 100],
        pageSize: "10",
        currentPage: 1
    };
    $scope.template = [{id:'all',text:"所有"},{id:'now',text:"立即执行"},{id:'time',text:"定时任务"}];

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
        $scope.setPagingData($scope.taskList ? $scope.taskList : [], pageSize, page);
    };


    $scope.search_task_info = function () {
        loading.open();
        sysService.search_task_info({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                $scope.taskList = res.data;
                $scope.pagingOptions.currentPage = 1;
                $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
            } else {
                errorModal.open(res.msg);
            }
        })
    };
    $scope.search_task_info();


    $scope.$watch('pagingOptions', function (newVal, oldVal) {
        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
    }, true);


    $scope.modify_task = function (row) {
        $state.go('modify_task',{task_id:row.entity.task_id})
    };


    $scope.delete_task = function (row) {
        //根据id删除系统
        var task_id = row.entity.task_id;
        confirmModal.open({
            text: "确定删除该任务吗？",
            confirmClick: function () {
                loading.open();
                sysService.delete_task({}, {task_id: task_id}, function (res) {
                    loading.close();
                    if (res.result) {
                        $scope.taskList.splice(row.rowIndex, 1);
                        msgModal.open("success", "删除任务成功！");
                        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
                    }
                    else {
                        errorModal.open(res.msg);
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
            {field: "task_name", displayName: "任务名称", width: 250},
            {field: "execute_type", displayName: "执行类型", width: 250},
            {field: "email", displayName: "报告邮箱", width: 250},
            {field: "platform", displayName: "平台", width: 250},
            {
                displayName: "操作",
                cellTemplate: '<div style="width:100%;padding-top:5px;text-align: center">' +
                '<span style="cursor: pointer" class="btn btn-xs btn-primary" ng-click="modify_task(row)">修改</span>&emsp;' +
                '<span style="cursor: pointer" class="btn btn-xs btn-danger" ng-click="delete_task(row)">删除</span>' +
                '<span style="cursor: pointer;margin-left:13px" class="btn btn-xs btn-danger" ui-sref="host_list({task_id:row.entity.task_id})">任务详情</span>' +
                '</div>'
            }
        ]
    };

}]);