controllers.controller("ListPage", function ($scope, $modal, errorModal, sysService, loading, confirmModal, msgModal) {
    $scope.course_list = [];
    $scope.index = 0;

    $scope.getAllCourse = function () {
        sysService.get_all_course({}, {}, function (res) {
            if (res.result){
                $scope.content_list = res.data
            }else{
                errorModal.open(['xxxxxx'])
            }
            $scope.content_detail = {
                title: $scope.content_list[$scope.index].title,
                tip: $scope.content_list[$scope.index].tip,
                image_base64: "data:image/jpeg;base64," + $scope.content_list[$scope.index].image,
            }
        })
    };
    $scope.getAllCourse();

    $scope.getContentDetail = function () {
        if ($scope.index + 1 < $scope.content_list.length){
            $scope.index = $scope.index + 1

        }else{
            $scope.index = 0
        }
         $scope.content_detail = {
                title: $scope.content_list[$scope.index].title,
                tip: $scope.content_list[$scope.index].tip,
                image_base64: "data:image/jpeg;base64," + $scope.content_list[$scope.index].image,
            };
        $scope.$apply();
    };


    window.setInterval($scope.getContentDetail,5000);

    $scope.filter_args = {
        title: ''
    };

    $scope.add = function () {
        var modalInstance = $modal.open({
        templateUrl: static_url + 'client/views/addCourse.html',
        windowClass: 'task_dialog',
        controller: 'addCourse',
        backdrop: 'static',
        resolve: {
                objectItem: function () {
                    return null
                }
            }
    });
    modalInstance.result.then(function () {
        $scope.getAllCourse();
        $scope.searchCourseList()
    });
    };

    $scope.searchCourseList = function(){
        sysService.search_course_list({}, $scope.filter_args, function (res) {
            if (res.result){
                $scope.course_list = res.data;
            }else{
                errorModal.open(['系统错误，联系管理员'])
            }
        })
    };

    $scope.searchCourseList();


    $scope.gridOption = {
        data: 'course_list',
        enablePaging: true,
        showFooter: true,
        pagingOptions: $scope.pagingOptions,
        totalServerItems: 'totalSerItems',
        columnDefs: [
            {field: 'title', displayName: '标题'},
            {field: 'tip', displayName: '备注'},
            {field: 'content', displayName: '内容'},
            {field: 'bk_biz_name', displayName: '业务'},
            {displayName:'操作',
            cellTemplate: '<div style="width:100%;text-align: center;padding-top: 5px;">' +
                '<span  ng-click="look(row.entity)" style="cursor: pointer">查询</span>&emsp;' +
                '<span  ng-click="modify(row.entity)" style="cursor: pointer">修改</span>&emsp;' +
                '<span  ng-click="delete(row.entity.id)" style="cursor: pointer">移除</span>' +
                '</div>'}
        ]
    };

    $scope.look = function (row_mes) {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/addCourse.html',
            windowClass: 'task_dialog',
            controller: 'addCourse',
            backdrop: 'static',
            resolve: {
                    objectItem: function () {
                        var obj_item = angular.copy(row_mes);
                        obj_item.is_show = true;
                        obj_item.is_update = false;
                        return obj_item
                    }
                }
        });
        modalInstance.result.then(function () {

        });
    };

    $scope.modify = function (row_mes) {
        var modalInstance = $modal.open({
        templateUrl: static_url + 'client/views/addCourse.html',
        windowClass: 'task_dialog',
        controller: 'addCourse',
        backdrop: 'static',
        resolve: {
                objectItem: function () {
                    var obj_item = angular.copy(row_mes);
                    obj_item.is_show = false;
                    obj_item.is_update = true;
                    return obj_item
                }
            }
        });
        modalInstance.result.then(function () {
            $scope.getAllCourse();
            $scope.searchCourseList()
        });
    };

    $scope.delete = function (row_id) {
        sysService.delete_course({}, {id: row_id}, function () {

        })
        $scope.getAllCourse();
        $scope.searchCourseList()
    }


});