controllers.controller("add_task", ["$scope", "loading", "$modal", "confirmModal", "sysService", "errorModal", "msgModal","$state", function ($scope, loading, $modal, confirmModal, sysService, errorModal, msgModal,$state) {

    $scope.biz_id = 1;
    $scope.tittle = "新增任务";
    $scope.ip_list = [];
    $scope.args = {
        task_name: '',
        execute_type: '',
        email: '',
        platform: '',
        ip_list: []
    };

    $scope.biz_list = [{id:1, name:"蓝鲸"},{id:2, name: 'fta'}];
    $scope.host_id = [];
    $scope.hostList = [];

    $scope.host_data = {
         1: [{id: 1, ip:"127.0.0.1", life_time: "one", cloud: "蓝鲸1", biz_id: 1},
            {id: 2, ip:"127.0.0.2", life_time: "two", cloud: "蓝鲸2",biz_id: 1},
            {id: 3, ip:"127.0.0.3", life_time: "three", cloud: "蓝鲸3",biz_id: 1},
            {id: 4, ip:"127.0.0.4", life_time: "four", cloud: "蓝鲸4",biz_id: 1},
            {id: 5, ip:"127.0.0.5", life_time: "five", cloud: "蓝鲸5",biz_id: 1},
            {id: 6, ip:"127.0.0.6", life_time: "six", cloud: "蓝鲸6",biz_id: 1}],
        2: [{id: 7, ip:"127.0.0.7", life_time: "one", cloud: "fta1",biz_id: 2},
            {id: 8, ip:"127.0.0.8", life_time: "two", cloud: "fta2",biz_id: 2},
            {id: 9, ip:"127.0.0.9", life_time: "three", cloud: "fta3",biz_id: 2},
            {id: 10, ip:"127.0.0.10", life_time: "four", cloud: "fta4",biz_id: 2},
            {id: 11, ip:"127.0.0.11", life_time: "five", cloud: "fta5",biz_id: 2},
            {id: 12, ip:"127.0.0.12", life_time: "six", cloud: "fta6",biz_id: 2}]
      };


    $scope.add_host = function () {
        if($scope.biz_id == ''){
             msgModal.open("info", "请先选择业务！");
             return
        }
        var modalInstance = $modal.open({
            templateUrl: static_url + 'client/views/addhost.html',
            windowClass: 'dialog_custom',
            controller: 'addhost',
            backdrop: 'static',
            resolve: {
                objectItem: function () {
                    return {biz: $scope.biz_id,host_id: $scope.host_id};
                }
            }
        });
        modalInstance.result.then(function (res) {
            $scope.host_id = [];
            $scope.new_ip_list = [];
            for(var j = 0; j < $scope.ip_list.length; j++){
                if($scope.ip_list[j].biz_id != $scope.biz_id){
                    $scope.new_ip_list.push($scope.ip_list[j]);
                    $scope.host_id.push($scope.ip_list[j].id.toString())
                }
            }
            var hosts = $scope.host_data[$scope.biz_id];
            for(var i = 0; i < hosts.length; i++){
                if(res.indexOf(hosts[i].id.toString()) != -1){
                    $scope.new_ip_list.push(hosts[i])
                    $scope.host_id.push(hosts[i].id.toString())
                }
            }
            $scope.ip_list = $scope.new_ip_list;
            $scope.args.ip_list = $scope.ip_list

        })
    };


    $scope.delete = function(host_id){
        var host_index = '';
        var ip_index = '';
        for (var i =0; i < $scope.host_id; i++){
            if(host_id.toString() == $scope.host_id[i]){
                host_index = i;
            }
        }
        $scope.host_id.splice(host_index, 1)

        for (var j = 0; j < $scope.ip_list.length; j++){
            if($scope.ip_list[j].id == host_id){
                ip_index = j;
            }
        }
        $scope.ip_list.splice(ip_index,1)

    };


     $scope.confirm = function () {
         if($scope.args.task_name == ''){
             msgModal.open('info',"请添加任务名称！");
             return
         }
         if($scope.args.execute_type == ''){
             msgModal.open('info',"请选择执行类型！");
             return
         }
         if($scope.args.email == ''){
             msgModal.open('info',"请添加邮箱！");
             return
         }
         if($scope.args.platform == ''){
             msgModal.open('info',"请添加执行平台！");
             return
         }
         if($scope.ip_list.length == 0){
             msgModal.open('info',"请添加主机！");
             return
         }
        loading.open();
        sysService.add_task({}, $scope.args, function (res) {
            loading.close();
            if (res.result) {
                msgModal.open('success', "添加任务成功")
                $state.go('home')
            } else {
                errorModal.open(res.msg);
            }
        });
    };


     $scope.cancel = function () {
         $state.go('home')
     }


}]);


