# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1546595232.639
_enable_loop = True
_template_filename = u'C:/Users/lenovo/Desktop/kkk/cw-tmp-top-bk/templates/base.html'
_template_uri = u'/base.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_token = context.get('csrf_token', UNDEFINED)
        STATIC_VERSION = context.get('STATIC_VERSION', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        APP_ID = context.get('APP_ID', UNDEFINED)
        LOGOUT_URL = context.get('LOGOUT_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html ng-app="myApp">\r\n<head>\r\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\r\n    <title>\u5609\u7ef4\u84dd\u9cb8\u5f00\u53d1\u6846\u67b6</title>\r\n    <meta name="description" content=""/>\r\n    <meta name="author" content=""/>\r\n    <link rel="shortcut icon" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'favicon.ico" type="image/x-icon">\r\n    <!-- bootstrap css -->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">\r\n    <!-- \u7981\u6b62bootstrap \u54cd\u5e94\u5f0f \uff08app\u6839\u636e\u81ea\u8eab\u9700\u6c42\u542f\u7528\u6216\u7981\u6b62bootstrap\u54cd\u5e94\u5f0f\uff09 -->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap_noresponsive.css" rel="stylesheet">\r\n    <!--\u63d2\u4ef6css-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/zTreeStyle.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/ng-grid.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/jquery-ui-1.10.4.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/toastr.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/kendo.common.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/kendo-default.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/kendo-datetime.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/select2.css" rel="stylesheet">\r\n\r\n    <!--\u5609\u4e3a\u84dd\u9cb8\u5f00\u53d1\u6846\u67b6UI-->\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/perfect-scrollbar.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/roboto.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/font-awesome.min.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/panel.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/feather.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/animate.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/urban.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/urban.skins.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/template.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/base-page.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/cw-left-menu.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/directive.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui-new/base-page.css" rel="stylesheet">\r\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui-new/cw-top-menu.css" rel="stylesheet">\r\n\r\n\r\n    <!-- \u8fd9\u4e2a\u662f\u5168\u5c40\u914d\u7f6e\uff0c\u5982\u679c\u9700\u8981\u5728js\u4e2d\u4f7f\u7528app_id\u548csite_url,\u5219\u8fd9\u4e2ajavascript\u7247\u6bb5\u4e00\u5b9a\u8981\u4fdd\u7559 -->\r\n    <script type="text/javascript">\r\n        var app_id = "')
        __M_writer(unicode(APP_ID))
        __M_writer(u'";\r\n        var site_url = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t  // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\r\n        var static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'"; // \u9759\u6001\u8d44\u6e90\u524d\u7f00\r\n        var current_user = "')
        __M_writer(unicode(request.user.username))
        __M_writer(u'";\r\n        var app_path = window.location.origin + site_url;\r\n    </script>\r\n</head>\r\n<body ng-controller="site" class="siteBody">\r\n<!--\u8bbf\u95ee\u63a5\u53e3\u7528\uff0c\u8bf7\u52ff\u5220\u9664-->\r\n<input type=\'hidden\' id="csrf" name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(unicode(csrf_token))
        __M_writer(u'\'>\r\n\r\n<div>\r\n    <!--\u9876\u90e8\u5bfc\u822a Start-->\r\n    <nav class="navbar navbar-default king-horizontal-nav2 top-nav" role="navigation">\r\n        <div class="container">\r\n            <div class="navbar-header logo">\r\n                <a class="navbar-brand logo-href" href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'">\r\n                    \u5f00\u53d1\u6846\u67b6\r\n                </a>\r\n                <div style="border-left:1px solid #eee;height:30px;position: absolute;top:15px;"></div>\r\n            </div>\r\n            <!--\u9876\u90e8\u83dc\u5355start-->\r\n            <div cw-top-menu="menuOption"></div>\r\n            <!--\u9876\u90e8\u83dc\u5355end-->\r\n            <!--\u767b\u9646\u6ce8\u9500start-->\r\n            <div style="position:absolute;right:0;top:0;overflow:auto;color: #ccc;width:190px;">\r\n                <img src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'img/getheadimg.jpg" class="nav-user-photo"\r\n                     style=" width:45px;height:45px;border:1px solid #ddd;"/>\r\n                <span class="user-info" style="color: #333">')
        __M_writer(unicode(request.user.username))
        __M_writer(u'</span>\r\n                <a class="io-fa icon-logoutcloudboot logout" href="')
        __M_writer(unicode(LOGOUT_URL))
        __M_writer(u'"></a>\r\n            </div>\r\n            <!--\u767b\u9646\u6ce8\u9500end-->\r\n        </div>\r\n    </nav>\r\n    <!--\u9876\u90e8\u5bfc\u822a End-->\r\n\r\n</div>\r\n<!-- \u56fa\u5b9a\u5bbd\u5ea6\u5c45\u4e2d start -->\r\n<div class="main-container">\r\n    <!--\u5de6\u4fa7\u5bfc\u822abegin-->\r\n    <!--<div cw-left-menu="menuOption"></div>-->\r\n    <!--<div class="main-content" id="main-content"-->\r\n         <!--style="position:absolute;left:15%;top:0;bottom: 0;width: 85%; overflow: hidden;margin-left: 0">-->\r\n        <!--<div id="top_nav2">-->\r\n            <!--<div id="locationPlaceHolder" style="font-size: 12px; color: #333;">-->\r\n            <!--</div>-->\r\n        <!--</div>-->\r\n        <!--<div id="ui-content-main" class="ui-content-main" ui-view-->\r\n             <!--style="padding:0;width:100%; position: absolute;top:35px;bottom: 0;overflow-y: hidden;height: auto !important;"></div>-->\r\n    <!--</div>-->\r\n    <!--\u5de6\u4fa7\u5bfc\u822aend-->\r\n    <!--\u5934\u90e8\u5bfc\u822abegin-->\r\n    <div class="main-content" id="main-content"style="overflow: hidden;">\r\n        <!--<div id="top_nav2">-->\r\n            <!--<div id="locationPlaceHolder" style="font-size: 12px; color: #333;">-->\r\n            <!--</div>-->\r\n        <!--</div>-->\r\n        <div id="ui-content-main" class="ui-content-main" ui-view\r\n             style="padding:0;width:100%; position: absolute;top:35px;bottom: 0;overflow-y: hidden;height: auto !important;"></div>\r\n    </div>\r\n    <!--\u5934\u90e8\u5bfc\u822aend-->\r\n</div>\r\n<!-- \u56fa\u5b9a\u5bbd\u5ea6\u8868\u5355\u5c45\u4e2d end -->\r\n<!-- \u5c3e\u90e8\u58f0\u660e start -->\r\n\r\n<!-- \u5c3e\u90e8\u58f0\u660e start -->\r\n<!-- jquery js  -->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.10.2.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.json-2.3.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-ui-1.10.4.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.ztree.all-3.5.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/kendo.all.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/select2.js" type="text/javascript"></script>\r\n<!-- bootstrap js  -->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/js/bootstrap.min.js" type="text/javascript"></script>\r\n<!--\u914d\u7f6ejs  \u52ff\u5220-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/settings.js?v=')
        __M_writer(unicode(STATIC_VERSION))
        __M_writer(u'" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/toastr.min.js" type="text/javascript"></script>\r\n<!--angular js-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular-resource.min.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/ui-bootstrap-tpls-0.12.0.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular-ui-router.min.js" type="text/javascript"></script>\r\n\r\n<!--\u8868\u683c\u63a7\u4ef6-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/ng-grid.js" type="text/javascript"></script>\r\n\r\n<!--\u5de6\u4fa7\u83dc\u5355js-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/leftmenu.js" type="text/javascript"></script>\r\n\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/init.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Services.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Directives.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Utilities_Services.js" type="text/javascript"></script>\r\n\r\n<!--\u81ea\u5b9a\u4e49\u914d\u7f6e\u529f\u80fd-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Config.js" type="text/javascript"></script>\r\n\r\n<!--\u786e\u8ba4\u63d0\u793a\u6846-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Confirm.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Message.js" type="text/javascript"></script>\r\n\r\n<!--\u9519\u8bef\u63d0\u793a\u6846-->\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Error.js" type="text/javascript"></script>\r\n\r\n\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/addSys.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/modifySys.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/syslog.js" type="text/javascript"></script>\r\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/sysconfig.js" type="text/javascript"></script>\r\n\r\n\r\n\r\n\r\n')
        __M_writer(unicode(self.body()))
        __M_writer(u'\r\n</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "29": 1, "30": 8, "31": 8, "32": 10, "33": 10, "34": 12, "35": 12, "36": 14, "37": 14, "38": 15, "39": 15, "40": 16, "41": 16, "42": 17, "43": 17, "44": 18, "45": 18, "46": 19, "47": 19, "48": 20, "49": 20, "50": 21, "51": 21, "52": 24, "53": 24, "54": 25, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29, "64": 30, "65": 30, "66": 31, "67": 31, "68": 32, "69": 32, "70": 33, "71": 33, "72": 34, "73": 34, "74": 35, "75": 35, "76": 36, "77": 36, "78": 37, "79": 37, "80": 42, "81": 42, "82": 43, "83": 43, "84": 44, "85": 44, "86": 45, "87": 45, "88": 51, "89": 51, "90": 58, "91": 58, "92": 68, "93": 68, "94": 70, "95": 70, "96": 71, "97": 71, "98": 109, "99": 109, "100": 110, "101": 110, "102": 111, "103": 111, "104": 112, "105": 112, "106": 113, "107": 113, "108": 114, "109": 114, "110": 116, "111": 116, "112": 118, "113": 118, "114": 118, "115": 118, "116": 119, "117": 119, "118": 121, "119": 121, "120": 122, "121": 122, "122": 123, "123": 123, "124": 124, "125": 124, "126": 127, "127": 127, "128": 130, "129": 130, "130": 132, "131": 132, "132": 133, "133": 133, "134": 134, "135": 134, "136": 135, "137": 135, "138": 138, "139": 138, "140": 141, "141": 141, "142": 142, "143": 142, "144": 145, "145": 145, "146": 148, "147": 148, "148": 149, "149": 149, "150": 150, "151": 150, "152": 151, "153": 151, "154": 156, "155": 156, "161": 155}, "uri": "/base.html", "filename": "C:/Users/lenovo/Desktop/kkk/cw-tmp-top-bk/templates/base.html"}
__M_END_METADATA
"""
