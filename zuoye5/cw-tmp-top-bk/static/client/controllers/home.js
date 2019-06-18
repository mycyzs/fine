controllers.controller("home", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal) {

    $scope.static_u = static_url;
    $scope.timeid = '';
    $scope.args = {
        sys_name: "",
        b_id: ''
    };

    $scope.current_url = window.location.href.split('#')[0];

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


    $scope.inits = function () {
        loading.open();
        sysService.search_init({}, $scope.args, function (res) {
            loading.close();

        })
    };
    $scope.inits();
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

    // 获取前十张图片
    $scope.books = [];
    $scope.search_book_info = function () {
        loading.open();
        sysService.search_book_info({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.books = res.data

            } else {
                errorModal.open(res.msg);
            }
            setTimeout(function () {
                autoMove('my-div');
                },600)
        })
    };
    $scope.search_book_info();

    $scope.la_search_book_info = function () {
        loading.open();
        sysService.la_search_book_info({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.books = res.data

            } else {
                errorModal.open(res.msg);
            }

        })
    };

    // setTimeout(function () {
    //                 autoMove('my-div');
    //             },600)

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
            window.clearInterval($scope.timeid);
            $scope.search_book_info();
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
            row.entity.name = res.name;
            row.entity.content = res.content;
            row.entity.comment = res.comment;
            row.entity.biz = res.biz;
            row.entity.creator = res.creator;
            row.entity.when_created = res.when_created;
            window.clearInterval($scope.timeid);
            $scope.search_book_info();
        })
    };

    $scope.detail = function (row) {
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/detail.html',
            windowClass: 'dialog_custom',
            controller: 'detail',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return row.entity;
                }
            }
        });
        modalInstance.result.then(function (res) {
            row.entity.name = res.name;
            row.entity.content = res.content;
            row.entity.comment = res.comment;
            row.entity.biz = res.biz;
            row.entity.creator = res.creator;
            row.entity.when_created = res.when_created;

        })
    };


    $scope.delete_sys = function (row) {
        //根据id删除系统
        var id = row.entity.id;
        confirmModal.open({
            text: "确定删除该课程吗？",
            confirmClick: function () {
                loading.open();
                sysService.delete_sys({}, {id: id}, function (res) {
                    loading.close();
                    if (res.result) {
                        $scope.hostList.splice(row.rowIndex, 1);
                        msgModal.open("success", "删除课程成功！");
                        $scope.getPagedDataAsync($scope.pagingOptions.pageSize, $scope.pagingOptions.currentPage);
                        window.clearInterval($scope.timeid);
                        $scope.search_book_info();
                    }
                    else {
                        errorModal.open(res.message);
                    }
                })
            }
        });

    };
    function InitMove(index) {
            $scope.imgs[index].style.opacity = '1';
            for (var i = 0; i < $scope.imgs.length; i++) {
                if (i != index) {
                    $scope.imgs[i].style.opacity = '0';
                }
            }
        }
    function autoMove(tagImg) {

        $scope.imgs = document.getElementsByClassName(tagImg);



        InitMove(0);


        $scope.timeid = setInterval(fMove, 3000);

    }
        var count = 1;

    function fMove() {
        if (count == $scope.imgs.length) {
            count = 0;
        }
        InitMove(count);
        count++;
        $scope.$apply()

    }

    $scope.up_pic = function () {

        var file = document.getElementById("kkk").files[0];
        var xhr = new XMLHttpRequest();
        var url = site_url + 'upload_pic/?book_id=' + $scope.args.b_id;
        xhr.open('POST', url, true);
        xhr.setRequestHeader('X-CSRFToken', $("#csrf").val());
        xhr.setRequestHeader("Accept", "*/*");

        xhr.onload = function (e) {
            if (this.status == 200) {
                alert("更新封面成功!!")
                window.location.reload()
            }
        }
        xhr.send(file)
    }

    $scope.need_id = function (row) {
        $scope.args.b_id = row.entity.id
    }

    $scope.gridOption = {
        data: "PagingData",
        enablePaging: true,
        enableColumnResize: true,
        showFooter: true,
        pagingOptions: $scope.pagingOptions,
        totalServerItems: 'totalSerItems',
        columnDefs: [
            {field: "name", displayName: "课程名称", width: 200},
            {field: "content", displayName: "课程内容", width: 180},
            {field: "comment", displayName: "备注", width: 220},
            {field: "creator", displayName: "创建者", width: 200},
            {field: "when_created", displayName: "创建时间", width: 220},
            {
                displayName: "操作",
                cellTemplate: '<div style="width:100%;padding-top:5px;text-align: center">' +
                '<div ng-click="need_id(row)" style="float: left;width: 80px;height: 20px;background:#9fa1e6;color: #fff;border: solid black 0.5px;margin-left: 5px"><input type="file" id="kkk" onchange="angular.element(this).scope().up_pic()"  multiple="" accept="image/png,imagge/jpg,image/jpeg,image/png,image/gif" name="dat-image" style="position: absolute;opacity: 0">上传封面</div>' +
                '<span style="cursor: pointer" class="btn btn-xs btn-primary" ng-click="detail(row)">查看</span>&emsp;' +
                '<span style="cursor: pointer;margin-left: 17px" class="btn btn-xs btn-danger" ng-click="modify_sys(row)">修改</span>' +
                '<span style="cursor: pointer;margin-left: 30px" class="btn btn-xs btn-danger" ng-click="delete_sys(row)">删除</span>' +
                '</div>'
            }
        ]
    };

}]);