# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1545966546.163
_enable_loop = True
_template_filename = u'C:/Users/lenovo/Desktop/ziliao/lizhihui/templates/base.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html ng-app="myApp">\n<head>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n    <title></title>\n    <meta name="description" content=""/>\n    <meta name="author" content=""/>\n    <link rel="shortcut icon" href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'favicon.ico" type="image/x-icon">\n    <!-- bootstrap css -->\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">\n    <!-- \u7981\u6b62bootstrap \u54cd\u5e94\u5f0f \uff08app\u6839\u636e\u81ea\u8eab\u9700\u6c42\u542f\u7528\u6216\u7981\u6b62bootstrap\u54cd\u5e94\u5f0f\uff09 -->\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/css/bootstrap_noresponsive.css" rel="stylesheet">\n    <!--\u63d2\u4ef6css-->\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/ng-grid.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/jquery-ui-1.10.4.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/toastr.min.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/kendo-default.min.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/kendo-datetime.min.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/select2.css" rel="stylesheet">\n\n    <!--\u5609\u4e3a\u84dd\u9cb8\u5f00\u53d1\u6846\u67b6UI-->\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/font-awesome.min.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/urban.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/urabn-ui/urban.skins.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/template.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/base-page.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/cw-left-menu.css" rel="stylesheet">\n    <link href="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'css/cw-ui/directive.css" rel="stylesheet">\n\n    <!-- \u8fd9\u4e2a\u662f\u5168\u5c40\u914d\u7f6e\uff0c\u5982\u679c\u9700\u8981\u5728js\u4e2d\u4f7f\u7528app_id\u548csite_url,\u5219\u8fd9\u4e2ajavascript\u7247\u6bb5\u4e00\u5b9a\u8981\u4fdd\u7559 -->\n    <script type="text/javascript">\n        var app_id = "')
        __M_writer(unicode(APP_ID))
        __M_writer(u'";\n        var site_url = "')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'";\t  // app\u7684url\u524d\u7f00,\u5728ajax\u8c03\u7528\u7684\u65f6\u5019\uff0c\u5e94\u8be5\u52a0\u4e0a\u8be5\u524d\u7f00\n        var static_url = "')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'"; // \u9759\u6001\u8d44\u6e90\u524d\u7f00\n        var current_user = "')
        __M_writer(unicode(request.user.username))
        __M_writer(u'";\n        var app_path = window.location.origin + site_url;\n    </script>\n</head>\n\n<body ng-controller="site" class="siteBody">\n<!--\u8bbf\u95ee\u63a5\u53e3\u7528\uff0c\u8bf7\u52ff\u5220\u9664-->\n<input type=\'hidden\' id="csrf" name=\'csrfmiddlewaretoken\' value=\'')
        __M_writer(unicode(csrf_token))
        __M_writer(u'\'>\n\n<div>\n    <div class="king-layout1-header">\n        <nav role="navigation" class="navbar navbar-default king-horizontal-nav2    f14 ">\n            <div class="container " style="width:100%;overflow:hidden;">\n                <div class="navbar-header">\n                    <button type="button" class="navbar-toggle collapsed navbar-toggle-sm" data-toggle="collapse"\n                            data-target="#king-horizontal-nav2-collapse">\n                        <span class="sr-only">Toggle navigation</span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                        <span class="icon-bar"></span>\n                    </button>\n                    <a class="navbar-brand" href="javascript:;">\n                        <img src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'img/logo3.png" alt=""\n                             class="logo"> </a>\n                </div>\n                <div class="collapse navbar-collapse navbar-responsive-collapse" id="king-horizontal-nav2-collapse">\n                    <ul class="nav navbar-nav">\n                        <li ng-class="{\'king-navbar-active\':pageUrl.indexOf(\'home\')>-1}"><a ui-sref="home" ng-click="goToUrl(\'home\')">\u9996\u9875</a></li>\n                        <li ng-class="{\'king-navbar-active\':pageUrl.indexOf(\'hostInfo\')>-1}"><a ui-sref="hostInfo" ng-click="goToUrl(\'hostInfo\')">\u4e3b\u673a\u72b6\u6001</a></li>\n                    </ul>\n                    <ul class="nav navbar-nav navbar-right">\n                        <li>\n                            <a href="javascript:;">\n                                <span>')
        __M_writer(unicode(request.user.username))
        __M_writer(u'</span>\n                            </a>\n                        </li>\n                    </ul>\n                </div>\n            </div>\n        </nav>\n    </div>\n</div>\n<!-- \u56fa\u5b9a\u5bbd\u5ea6\u5c45\u4e2d start -->\n<div class="main-container">\n    <div class="main-content" id="main-content"\n         style="overflow: hidden;width:100%;height: 100%;">\n        <div id="ui-content-main" class="ui-content-main" ui-view\n             style="padding:0;width:100%; position: absolute;top:0;bottom: 0;overflow-y: hidden;height: auto !important;">\n        </div>\n    </div>\n</div>\n<!-- \u56fa\u5b9a\u5bbd\u5ea6\u8868\u5355\u5c45\u4e2d end -->\n<!-- \u5c3e\u90e8\u58f0\u660e start -->\n\n<!-- \u5c3e\u90e8\u58f0\u660e start -->\n<!-- jquery js  -->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-1.10.2.min.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery.json-2.3.min.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/jquery-ui-1.10.4.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/kendo.all.min.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/select2.js" type="text/javascript"></script>\n<!-- bootstrap js  -->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'assets/bootstrap-3.3.4/js/bootstrap.min.js" type="text/javascript"></script>\n<!--\u914d\u7f6ejs  \u52ff\u5220-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/settings.js?v=')
        __M_writer(unicode(STATIC_VERSION))
        __M_writer(u'" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/toastr.min.js" type="text/javascript"></script>\n<!--angular js-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular.min.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular-resource.min.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/ui-bootstrap-tpls-0.12.0.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/angular-ui-router.min.js" type="text/javascript"></script>\n\n<!--\u8868\u683c\u63a7\u4ef6-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/ng-grid.js" type="text/javascript"></script>\n\n<!--\u5de6\u4fa7\u83dc\u5355js-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/angular_base/leftmenu.js" type="text/javascript"></script>\n\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/init.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Services.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Directives.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/Utilities_Services.js" type="text/javascript"></script>\n\n<!--\u81ea\u5b9a\u4e49\u914d\u7f6e\u529f\u80fd-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Config.js" type="text/javascript"></script>\n\n<!--\u786e\u8ba4\u63d0\u793a\u6846-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Confirm.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Message.js" type="text/javascript"></script>\n\n<!--\u9519\u8bef\u63d0\u793a\u6846-->\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/Error.js" type="text/javascript"></script>\n')
        __M_writer(unicode(self.body()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "28": 1, "29": 8, "30": 8, "31": 10, "32": 10, "33": 12, "34": 12, "35": 14, "36": 14, "37": 15, "38": 15, "39": 16, "40": 16, "41": 17, "42": 17, "43": 18, "44": 18, "45": 19, "46": 19, "47": 22, "48": 22, "49": 23, "50": 23, "51": 24, "52": 24, "53": 25, "54": 25, "55": 26, "56": 26, "57": 27, "58": 27, "59": 28, "60": 28, "61": 32, "62": 32, "63": 33, "64": 33, "65": 34, "66": 34, "67": 35, "68": 35, "69": 42, "70": 42, "71": 57, "72": 57, "73": 68, "74": 68, "75": 91, "76": 91, "77": 92, "78": 92, "79": 93, "80": 93, "81": 94, "82": 94, "83": 95, "84": 95, "85": 97, "86": 97, "87": 99, "88": 99, "89": 99, "90": 99, "91": 100, "92": 100, "93": 102, "94": 102, "95": 103, "96": 103, "97": 104, "98": 104, "99": 105, "100": 105, "101": 108, "102": 108, "103": 111, "104": 111, "105": 113, "106": 113, "107": 114, "108": 114, "109": 115, "110": 115, "111": 116, "112": 116, "113": 119, "114": 119, "115": 122, "116": 122, "117": 123, "118": 123, "119": 126, "120": 126, "121": 127, "122": 127, "128": 122}, "uri": "/base.html", "filename": "C:/Users/lenovo/Desktop/ziliao/lizhihui/templates/base.html"}
__M_END_METADATA
"""
