controllers.controller("site", ["$scope", "$rootScope", function ($scope, $rootScope) {

    $scope.mysqlMenu = [
        {
            displayName: "CMDB管理", iconClass: "fa fa-calendar", children: [
                {displayName: "系统信息", url: "#/sysInfo"},
            ]
        },
        {
            displayName: "巡检管理", iconClass: "fa fa-medkit", children: [
                {
                    displayName: "标准管理", children: [
                        {displayName: "模板管理", url: "#/model"}
                    ]
                },
            ]
        },
    ];

    $scope.oracleMenu = [
        {
            displayName: "CMDB管理", iconClass: "fa fa-calendar", children: [
                {displayName: "系统信息", url: "#/oracleSysInfo"},

            ]
        },


    ];

    $scope.settingMenu = [

        {
            displayName: "系统配置", iconClass: "fa fa-cog", children: [
                {displayName: "平台账号", url: "#/platformAccount"},
            ]
        },
    ];


    $scope.allMenus = [
        //MySQL菜单部分
        {pid: 1, url: "sysInfo"},
        {pid: 1, url: "clusterInfo"},
        {pid: 1, url: "instanceInfo"},
        {pid: 1, url: "instanceInstall"},
        {pid: 1, url: "MasterSlaveInstall"},
        {pid: 1, url: "slaveInstall"},
        {pid: 1, url: "lvsInfo"},
        {pid: 1, url: "qsInfo"},
        {pid: 1, url: "qsInstall"},
        {pid: 1, url: "lvsInstall"},
        {pid: 1, url: "middleInstallLog"},
        {pid: 1, url: "middleInstallDetail"},
        {pid: 1, url: "middleParamModify"},
        {pid: 1, url: "ddbProcessManage"},
        {pid: 1, url: "mhaDeploy"},
        {pid: 1, url: "mhaInfo"},
        {pid: 1, url: "mhaProcessManage"},
        {pid: 1, url: "accountinfo"},
        {pid: 1, url: "accountrequest"},
        {pid: 1, url: "OracleDataDump"},
        {pid: 1, url: "executeSql"},
        {pid: 1, url: "sqlHistory"},
        {pid: 1, url: "installLog"},
        {pid: 1, url: "installDetail"},
        {pid: 1, url: "sqlRule"},
        {pid: 1, url: "instanceRelate"},
        {pid: 1, url: "relateDetail"},
        {pid: 1, url: "mysqlParamModify"},
        {pid: 1, url: "CheckTaskMain1"},
        {pid: 1, url: "CheckTaskReport1"},
        {pid: 1, url: "CheckTaskDbReport1"},
        {pid: 1, url: "CheckTemplateMain1"},
        {pid: 1, url: "CheckItemMain1"},
        {pid: 1, url: "mysqlDataDump"},
        {pid: 1, url: "instanceStartStop"},
        {pid: 1, url: "instanceUpgrade"},
        {pid: 1, url: "CheckTaskItemReport1"},



        //Oracle菜单部分
        {pid: 2, url: "oracleSysInfo"},
        {pid: 2, url: "oracleClusterInfo"},
        {pid: 2, url: "oracleInstanceInfo"},
        {pid: 2, url: "accountinfo"},
        {pid: 2, url: "accountRequestO"},
        {pid: 2, url: "oracleSqlExec"},
        {pid: 2, url: "oracleSqlRule"},
        {pid: 2, url: "oracleSqlHistory"},
        {pid: 2, url: "CheckTaskMain2"},
        {pid: 2, url: "CheckTaskReport2"},
        {pid: 2, url: "CheckTemplateMain2"},
        {pid: 2, url: "CheckItemMain2"},
        {pid: 2, url: "CheckTaskItemReport2"},
        {pid: 2, url: "CheckTaskDbReport2"},


        //系统配置菜单部分
        {pid: 3, url: "settings"},
        {pid: 3, url: "platformAccount"},
        {pid: 3, url: "mysqlParam"},
        {pid: 3, url: "myCnfTemplate"},
        {pid: 3, url: "operateRecord"},

    ];

    $scope.realMenu = [];
    $scope.menuOption = {
        data: 'realMenu',
        locationPlaceHolder: '#locationPlaceHolder',
        adaptBodyHeight: CWApp.HeaderHeight + CWApp.FooterHeight
    };
    // $scope.isTab = 0;
    // $scope.menuList = ['MySQL','Oracle','系统管理'];
    $scope.openUrl = function (i, is_go) {
        if (i == 1) {
            $(".list_btn2").css("border-bottom", "");
            $(".list_btn3").css("border-bottom", "");
            $(".list_btn1").css("border-bottom", "5px solid #FAAF19");
            $scope.realMenu = angular.copy($scope.mysqlMenu);
            if (is_go)
                window.location.href = "#/sysInfo"
        }

        if (i == 2) {
            $(".list_btn1").css("border-bottom", "");
            $(".list_btn3").css("border-bottom", "");
            $(".list_btn2").css("border-bottom", "5px solid #FAAF19");
            $scope.realMenu = angular.copy($scope.oracleMenu);
            if (is_go)
                window.location.href = "#/oracleSysInfo"
        }
        if (i == 3) {
            $(".list_btn1").css("border-bottom", "");
            $(".list_btn2").css("border-bottom", "");
            $(".list_btn3").css("border-bottom", "5px solid #FAAF19");
            $scope.realMenu = angular.copy($scope.settingMenu);
            if (is_go)
                window.location.href = "#/settings"
        }
        ;


        $("#top_nav2").css("display", "block");
        $("#menus").css("display", "block");
        // $("#main-content").css("left", "15%");
        // $("#main-content").css("width", "85%");
        setTimeout(function () {
            $("#ui-content-main").css("top", "35px");
            var e = document.getElementById("sidebar_cwLeftMenu");
            var d = document.getElementById("sidebar-collapse_cwLeftMenu");
            var leftArrow = 'fa fa-angle-double-left fa-lg hidden-menu-arrow';
            var rightArrow = 'fa fa-angle-double-right fa-lg show-menu-arrow';
            if ($(e).hasClass("menu-min")) {
                $(".fa.fa-chevron-down.menu-icon-showsubmenu.rowOne").css('display', 'none');
                $(".main-content").css('width', '96%');
                $(".main-content").css('left', '4%');
                $(e).addClass("menu-min");
                $(e).addClass("menu-min-ul");
                $(d).removeClass(leftArrow);
                $(d).addClass(rightArrow);
            } else {
                $(".fa.fa-chevron-down.menu-icon-showsubmenu.rowOne").css('display', 'block');
                $(".main-content").css('width', '85%');
                $(".main-content").css('left', '15%');
                $(e).removeClass("menu-min");
                $(e).removeClass("menu-min-ul");
                $(d).removeClass(rightArrow);
                $(d).addClass(leftArrow);
            }
        }, 100)
    };
    $scope.setNoMenu = function () {
        $(".list_btn1").css("border-bottom","");
        $(".list_btn2").css("border-bottom","");
        $(".list_btn3").css("border-bottom","");
        console.log(1);
        $("#menus").css("display", "none");
        $("#main-content").css("left", "0");
        $("#ui-content-main").css("top", "0");
        $("#top_nav2").css("display", "none");
        $("#main-content").css("width", "100%");
    };

    var href = window.location.href.split("#/");
    if (href.length > 1) {
        if (href[1] == "home") {
            $scope.setNoMenu();
        }
        var temp_href = href[1];
        for (var i in $scope.allMenus) {
            if ($scope.allMenus[i].url == temp_href.split("?")[0]) {
                $scope.openUrl($scope.allMenus[i].pid, false);
                break;
            }
            else {
            }
        }
    }
    else {
        $scope.setNoMenu();
    }

    //切换状态
    function changeTab() {
        //改变切换状态
        $('.submenu').find('li').click(function () {
            $(this).find('a').addClass('active_left');
            $(this).siblings('li').find('a').removeClass('active_left');
            $(this).parent().parent().siblings().find('a').removeClass('active_left');
        })
    };
    setTimeout(function () {
        changeTab();
    }, 2500);


}]);