(function (window) {
    var leftMenu = angular.module('rgLeftMenu', []);
    leftMenu.directive('rgLeftMenu', function ($timeout) {
        return {
            require: '?ngModel',
            template: '<div id="rg_menu"><ul class="fir_ul">\
                <li class="fir_li" ng-repeat="i in rg_menuList">\
                    <a ng-click="check_fir($index,$event)" class="fir_a"><span class="rg_i"><i class="{{ i.iconClass }}"></i></span><span class="rg_fir_title" title="{{ i.displayName }}" ng-bind="i.displayName"></span></a>\
                    <ul ng-if="i.children" class="sec_ul">\
                        <li ng-repeat="x in i.children">\
                            <a ng-click="check_sec(x.url,$event)" ng-bind="x.displayName"></a>\
                        </li>\
                    </ul>\
                </li>\
            </ul></div>',
            link: function ($scope, el, attr) {
                $scope.rg_menuList = [];
                var option_data = $scope.$eval(attr.rgLeftMenu);
                $scope.$watch(attr.rgLeftMenu, function (a) {
                    $scope.rg_menuList = a;
                    $timeout(function () {
                        $scope.first_url()
                    },200)
                }, true);
                $scope.op_dict = {};
                $scope.check_fir = function (index, e) {
                    var obj_tag = e.target;
                    var i = $scope.rg_menuList[index];
                    if (i.children) {
                        if ($(e.target)[0].tagName != 'A') {
                            obj_tag = $(e.target).parents('a')[0]
                        }
                        var ul_h = i.children.length * 30 + 'px';
                        if ($scope.op_dict[index]) {
                            $(obj_tag).siblings().css('height', '0px');
                            $($(obj_tag).parent('.fir_li')).removeClass('rg_active');
                            $scope.op_dict = {};
                            $scope.op_dict[index] = false;
                        } else {
                            $(obj_tag).siblings().css('height', ul_h);
                            $($(obj_tag).parent('.fir_li')).addClass('rg_active');
                            $($(obj_tag).parent('.fir_li')).siblings().removeClass('rg_active');
                            $(obj_tag).parents('.fir_li').siblings().children('.sec_ul').css('height', '0px');
                            $scope.op_dict = {};
                            $scope.op_dict[index] = true;
                        }

                    } else {
                        window.location.hash = i.url
                    }
                };
                $scope.check_sec = function (i, e) {
                    var obj_tag = e.target;
                    if ($(e.target)[0].tagName == 'A') {
                        obj_tag = $(e.target).parents('li')[0]
                    }
                    window.location.hash = i;
                    $('.sec_ul li').removeClass('rg_active');
                    $(obj_tag).addClass('rg_active')
                };
                $scope.first_url = function () {
                    var now_hash = window.location.hash;
                    for (i in $scope.rg_menuList) {
                        if ($scope.rg_menuList[i].url == now_hash) {
                            $('.fir_ul>li').removeClass('rg_active');
                            $('.fir_ul>li li').removeClass('rg_active');
                            $($('.fir_ul>li')[i]).addClass('rg_active');
                            return
                        }
                        for (x in $scope.rg_menuList[i].children) {
                            if ($scope.rg_menuList[i].children[x].url == now_hash) {
                                $scope.op_dict[i] = true;
                                var ul_h = $scope.rg_menuList[i].children.length * 30 + 'px';
                                $('.fir_ul>li .sec_ul').css('height', '0');
                                $($($('.fir_ul>li')[i]).children('.sec_ul')).css('height', ul_h);
                                $('.fir_ul>li').removeClass('rg_active');
                                $('.fir_ul>li li').removeClass('rg_active');
                                $($('.fir_ul>li')[i]).addClass('rg_active');
                                $($($($('.fir_ul>li')[i]).children('.sec_ul')).children()[x]).addClass('rg_active');
                                return
                            }
                        }
                    }
                };


                function get_local_style(){
                    return 'sec_style';
                    // return localStorage.rg_style ? localStorage.rg_style :'first_style'
                }

                $('.change_style').mouseenter(function () {
                    $('#rg_nav_right #rg_logout .change_style').addClass('rghover')
                });
                $('.change_style').mouseleave(function () {
                    $('#rg_nav_right #rg_logout .change_style').removeClass('rghover')
                });
                $('.change_style li').mouseenter(function () {
                    var class_style = $(this).attr('class_style');
                    $('.siteBody').attr('class','siteBody left_style '+class_style)
                });
                $('.change_style li').mouseleave(function () {
                    $('.siteBody').attr('class','siteBody left_style '+get_local_style())
                });

                $('.siteBody').attr('class','siteBody left_style '+get_local_style());

                $('.change_style li').click(function () {
                    var class_style = $(this).attr('class_style');
                    localStorage.rg_style = class_style;
                    $('.siteBody').attr('class','siteBody left_style '+class_style);
                    $('#rg_nav_right #rg_logout .change_style').removeClass('rghover')
                })

            }
        }
    });
}(window));