controllers.controller("monitor", ["msgModal", "$scope", "loading", "sysService", "$modal", "confirmModal", "$stateParams", function (msgModal, $scope, loading, sysService, $modal, confirmModal, $stateParams) {
    $scope.search = function () {
        loading.open();
        sysService.get_server_monitor({}, $stateParams, function (res) {
            loading.close();
            if (res.result) {
                $scope.make_load(res.line);
                $scope.make_pie(res.mem_data);
                $scope.dis_data = res.dis_data
            } else {
                errorModal.open([res['error']])
            }
        })
    };
    $scope.dis_data = [];
    $scope.search();

    $scope.every_search = function () {
        sysService.get_server_monitor({}, $stateParams, function (res) {
            if (res.result) {
                $scope.make_load(res.line);
                $scope.make_pie(res.mem_data);
                $scope.dis_data = res.dis_data;
                if (window.location.hash.split('?')[0] == '#/monitor') {
                    setTimeout(function () {
                        $scope.every_search()
                    }, 60000)
                }
            } else {
                errorModal.open([res['error']])
            }
        })
    };
    setTimeout(function () {
        $scope.every_search()
    }, 60000);

    $scope.make_load = function (data) {
        Highcharts.chart('line_chart', {
            title: {
                text: '负载情况'
            },
            yAxis: {},
            xAxis: {
                categories: data['title']
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: '5分钟负载情况',
                data: data['data']
            }],
            tooltip: {
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:f}</b></td></tr>',
                headerFormat: ""
            }
        });
    };
    $scope.make_pie = function (data) {
        Highcharts.chart('pie_container', {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: '内存使用情况'
            },
            exporting: {
                enabled: false
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    }
                }
            },
            series: [{
                name: '',
                colorByPoint: true,
                data: [{
                    name: '已用内存容量(G)',
                    y: data['used']*1,
                    sliced: true,
                    selected: true
                }, {
                    name: '剩余内存容量(G)',
                    y: data['free']*1,
                }]
            }]
        });
    }
}]);
