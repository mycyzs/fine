controllers.controller("host_list", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", "$stateParams", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal, $stateParams) {
    $scope.task_id = $stateParams.task_id;

    $scope.pagingOptions = {
        pageSizes: [10, 50, 100],
        pageSize: "10",
        currentPage: 1
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


    $scope.search_host_list = function () {
        loading.open();
        sysService.search_host_list({}, {task_id: $scope.task_id}, function (res) {
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
    $scope.search_host_list();



     $scope.gridOption = {
        data: "PagingData",
        enablePaging: true,
        enableColumnResize: true,
        showFooter: true,
        pagingOptions: $scope.pagingOptions,
        totalServerItems: 'totalSerItems',
        columnDefs: [
            {field: "ip", displayName: "主机ip", width: 500},
            {field: "life_time", displayName: "生命周期", width: 500},
            {field: "cloud", displayName: "云区域", width: 500},
        ]
    };

}]);


