controllers.controller("check_s", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", "$stateParams", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal, $stateParams) {


    $('#daterangepicker_demo2').daterangepicker({

        "timePicker": true,
        "timePicker24Hour": true,
        "linkedCalendars": false,
        "autoUpdateInput": false,
        "locale": {
            format: 'YYYY-MM-DD HH:mm:ss',
            separator: ' ~ ',
            applyLabel: "应用",
            cancelLabel: "取消",
            resetLabel: "重置",
        }
    }, function (start, end, lable) {
        beginTimeStore = start;
        endTimeStore = end;
        alert(this.startDate.format(this.locale.format));
        alert(this.endDate.format(this.locale.format));



         sysService.search_load({}, {start:this.startDate.format(this.locale.format),end:this.endDate.format(this.locale.format),host_id:$stateParams.host_id}, function (res) {
            if (res.result) {
                $scope.load_data = res.load_data;
                $scope.db_change = res.load_data.data;
                $scope.dbReports.xAxis.categories = res.load_data.x;
            } else {
                errorModal.open(res.message);
            }
        });




    });

    $scope.search = function () {
        loading.open();
        sysService.search_info({}, $stateParams, function (res) {
            loading.close();
            if (res.result) {
                $scope.load_data = res.load_data;
                $scope.men = res.men;
                $scope.disk = res.disk;
                $scope.db_change = res.load_data.data;
                $scope.dbReports.xAxis.categories = res.load_data.x;

            } else {
                errorModal.open(res.message);
            }
        });
    }

    $scope.search();


    $scope.every_min = function () {
        sysService.search_info({}, $stateParams, function (res) {
            if (res.result) {
                $scope.load_data = res.load_data;
                $scope.men = res.men;
                $scope.disk = res.disk;
                $scope.db_change = res.load_data.data;
                $scope.dbReports.xAxis.categories = res.load_data.x;
                if (window.location.hash.split("?")[0] == '#/check_s') {
                    setTimeout(function () {
                        $scope.every_min()

                    }, 60000)
                }

            } else {
                errorModal.open(res.message);
            }
        });

    };


    setTimeout(function () {
        $scope.every_min()

    }, 60000);

    $scope.dbReports = {
        data: "db_change",
        chart: {type: 'line'},
        title: {text: '5分钟平均负载(近一个小时)', enabled: true},
        xAxis: {
            categories: []
        },
        //提示框位置和显示内容
        tooltip: {
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:f}</b></td></tr>',
            headerFormat: ""
        }
    };


    $scope.mysql_pie = {
        data: "men",
        title: {text: '内存使用情况', enabled: true},
        unit: "",
        size: "200px"
    };


    //获取mysql、oracle的数量
    $scope.get_count = function () {
        loading.open();
        sysService.get_count({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.db_change = res.data;
                $scope.dbReports.xAxis.categories = res.data.cat;

            } else {
                errorModal.open(res.message);
            }
        });
    };

    //$scope.get_count();


    //
    //   $scope.get_count_zhu = function () {
    //     loading.open();
    //     sysService.get_count_zhu({}, {}, function (res) {
    //         loading.close();
    //         if (res.result) {
    //             $scope.test_column = res.data
    //
    //         }else {
    //             errorModal.open(res.message);
    //         }
    //     });
    // };
    //
    //   $scope.get_count_zhu();
    //
    //
    // $scope.test_chart = {
    //     //柱状图标题
    //     title: {text: '服务器', enabled: false},
    //     //y轴
    //     yAxis: {
    //         title: {text: '数目'}, //y轴标题
    //         lineWidth: 2, //基线宽度1
    //         //tickPositions: [0, 1, 2, 3, 4]
    //     },
    //     //提示框位置和显示内容
    //     tooltip: {
    //         headerFormat: '<table\>',
    //         pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
    //         '<td style="padding:0"><b>{point.y:f} 台</b></td></tr>',
    //         footerFormat: '</table>',
    //         shared: true,
    //         useHTML: true,
    //         positioner: function () {
    //             return {x: 80, y: 80}
    //         }
    //     },
    //     data: "test_column"
    // };


}]);


