controllers.controller("test", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal) {

    $scope.get_count_obj = function () {
        loading.open();
        sysService.get_count({}, {}, function (res) {
            loading.close();
            if (res.result) {
                $scope.objs = res.data;
                $scope.parse_data()
                // $scope.data_list = res.data
                // $scope.dbReports.xAxis.categories = res.cat;
            } else {
                errorModal.open(res.message);
            }
        });
    };
    $scope.get_count_obj();

    $scope.dict = {};
    $scope.datas_list = [];
    $scope.parse_data = function(){

        for(var key in $scope.objs){
            debugger
            $scope.dict['key' + key] = $scope.objs[key]['data']

            $scope.dbReports.data = "dict.key" + key
            $scope.dbReports.title.text = $scope.objs[key]['name']
            $scope.dbReports.xAxis.categories = $scope.objs[key]['cat']
            $scope.datas_list.push({my_key: angular.copy($scope.dbReports)})
        }

    };

     $scope.dbReports = {
        data: "data_list",
        chart: {type: 'line'},
        title: {text: '访客量', enabled: true},
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

}]);


