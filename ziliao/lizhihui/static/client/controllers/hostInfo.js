controllers.controller("hostInfo", function ($scope, loading, sysService) {
    $scope.serverPerforms = [];
    $scope.filterObj = {
        appID: "",
        ip: ""
    };
    $scope.is_search = false;
    $scope.appList = [];
    $scope.performObj = {};
    $scope.init = function () {
        loading.open();
        sysService.get_app_list({}, {}, function (res) {
            loading.close();
            $scope.appList = res.data;
        })
    };

    $scope.init();


    $scope.searchList = function () {
        loading.open();
        sysService.search_server_perform_list({}, $scope.filterObj, function (res) {
            loading.close();
            if (res.result) {
                $scope.is_search = true;
                $scope.serverPerforms = res.data;
                $scope.performObj = res.perform_obj;
                angular.forEach($scope.serverPerforms, function (i) {
                    i.chartOptions = angular.extend({
                        chart: {type: 'line'},
                        title: {text: '近1小时主机资源使用情况（%）', enabled: true},
                        xAxis: {
                            categories: []
                        },
                        //提示框位置和显示内容
                        tooltip: {
                            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                            '<td style="padding:0"><b>{point.y:f}</b></td></tr>',
                            headerFormat: ""
                        }
                    }, {
                        data: i.name,
                        xAxis: {categories: i.categories}
                    });
                    console.log(i.chartOptions)
                })
            }
        })
    };

    $scope.highOption = {
        chart: {type: 'line'},
        title: {text: '近1小时主机资源使用情况（%）', enabled: true},
        xAxis: {
            categories: []
        },
        //提示框位置和显示内容
        tooltip: {
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:f}</b></td></tr>',
            headerFormat: ""
        }
    }

});