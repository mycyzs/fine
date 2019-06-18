controllers.controller("addhost", ["$scope","loading","$modalInstance","msgModal","sysService","errorModal","objectItem",function ( $scope,loading,$modalInstance,msgModal,sysService,errorModal,objectItem) {
    $scope.title = "选择主机";
    $scope.args = {
        ip: "",
        addr_ip: ""
    };
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
    $scope.hostList = [];

    $scope.init_data = function(){
        $scope.hostList = $scope.host_data[objectItem.biz]
    };

    $scope.init_data();

    $scope.init_checked_host = function(){
        var init_host = objectItem.host_id;
        var suns = document.getElementsByName("sun_ck");
        var flag = 0;
        if(init_host.length > 0){
            for (var i = 0; i < suns.length; i++) {
                if(init_host.indexOf(suns[i].value) != -1){
                    suns[i].checked = true;
                    flag = flag + 1
                    }
                }
        }
        if(suns.length != 0 && suns.length == flag){
            var box = document.getElementById("thead_ck");
             box.checked = true
        }
    };
    setTimeout($scope.init_checked_host,800);

    $scope.check = function(){
        var box = document.getElementById("thead_ck");
        var suns = document.getElementsByName("sun_ck");
        if(box.checked == false){
            for (var i = 0; i < suns.length; i++) {
                   suns[i].checked = false;
                }
        }else {
           for (var i = 0; i < suns.length; i++) {
                   suns[i].checked = true;
                }
        }
    };


    $scope.check_sum = function(){
        var box = document.getElementById("thead_ck");
        var suns = document.getElementsByName("sun_ck");
        var checked_host = [];
        for(var i = 0;i < suns.length; i++){
            if(suns[i].checked == true){
                checked_host.push(suns[i].value)
            }
        }
        if(suns.length == checked_host.length){
            box.checked = true
        }else {
            box.checked = false
        }
    };


    $scope.search_ip = function(){
        var box = document.getElementById("thead_ck");
        box.checked = false
        $scope.hostList = $scope.host_data[objectItem.biz];
        $scope.newList = [];
        for(var i = 0; i < $scope.hostList.length; i++){
            if($scope.hostList[i].ip.indexOf($scope.args.addr_ip) >= 0){
                $scope.newList.push($scope.hostList[i])
            }
        }
        $scope.hostList = $scope.newList;
        setTimeout($scope.init_checked_host,800);
    };

    $scope.confirm = function () {
        var suns = document.getElementsByName("sun_ck");
        var checked_ip = [];
        for(var i = 0;i < suns.length; i++){
            if(suns[i].checked == true){
                checked_ip.push(suns[i].value)
            }
        }
        $modalInstance.close(checked_ip);
    };

    $scope.cancel = function () {
        $modalInstance.dismiss("cancel");
    };





}]);