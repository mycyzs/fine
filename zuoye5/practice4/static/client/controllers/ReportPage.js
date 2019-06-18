controllers.controller("ReportPage", function ($scope, $modal, errorModal, sysService, loading, confirmModal, msgModal) {
    $scope.filter_args = {
        bk_biz_id: '',
        title: ''
    };
    $scope.chart_list = [];
    $scope.biz_list =[]

        $scope.searchBiz = function(){
        sysService.search_biz({}, {}, function (res) {
            if (res.result){
                $scope.biz_list = res.data
            }else{
                errorModal.open(['系统错误，联系管理员'])
            }
        })
    };
    $scope.searchBiz();

    $scope.list2 = {
        data: "data2",
        chart: {type: 'line'},//数据列类型，支持 area, areaspline, bar, column, line, pie, scatter or spline
        title: {text: '折线图示例', enable:true},
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
    $scope.dict={};
    $scope.searchReport = function () {
        sysService.search_report({}, $scope.filter_args, function (res) {
            $scope.chart_list = [];
            if (res.result){
                $scope.data_list = res.data;
                for (var i=0;i<$scope.data_list.length;i++){
                    $scope.dict['abc' + i] = $scope.data_list[i].data;
                    $scope.list2.data = "dict.abc"+i;
                    $scope.list2.xAxis.categories = $scope.data_list[i].categories;
                    $scope.list2.title.text = $scope.data_list[i].data[0].name;
                    $scope.chart_list.push({"chart": angular.copy($scope.list2)})
                }
            }else{
                errorModal.open(['error'])
            }
        })
    }
});