controllers.controller("home", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal","$state", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal, $state) {

    $scope.args = {
        sys_name: "",
        sys_code: "",
        owner: "",
        selected_id: ""
    };

    //内容显示页数和数量
    $scope.PagingData = [];
    $scope.totalSerItems = 0;

    $scope.pagingOptions = {
        pageSizes: [10, 50, 100],
        pageSize: "10",
        currentPage: 1
    };
    $scope.template = [{id:1,text:"aaa"},{id:2,text:"bbb"}];

    $scope.templateOption = {
        data: "template",
        multiple: false,
    };


    $scope.inits = function () {
        loading.open();
        sysService.search_init({}, $scope.args, function (res) {
            loading.close();

        })
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

    $scope.modify_syss = function () {

        sysService.search_aa_info({}, {}, function (res) {
                if(res.result){

                }

        })
    };
    $scope.modify_syss();

    $scope.modify_sys = function () {

        window.open('/open_test')

    };

     $scope.delete_sys = function () {

        window.open('/down_load_picture')

    };


    $scope.gridOption = {
        data: "PagingData",
        enablePaging: true,
        enableColumnResize: true,
        showFooter: true,
        pagingOptions: $scope.pagingOptions,
        totalServerItems: 'totalSerItems',
        columnDefs: [
            {field: "sys_name", displayName: "名称", width: 360},
            {field: "owners", displayName: "负责人", width: 380},
            {
                displayName: "操作",
                cellTemplate: '<div style="width:100%;padding-top:5px;text-align: center">' +
                '<span style="cursor: pointer" class="btn btn-xs btn-primary" ng-click="modify_sys()">二维码</span>&emsp;' +
                '<span style="cursor: pointer" class="btn btn-xs btn-danger" ng-click="delete_sys()">下载</span>' +
                '</div>'
            }
        ]
    };

}]);