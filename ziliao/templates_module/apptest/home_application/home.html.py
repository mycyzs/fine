# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1545964950.63
_enable_loop = True
_template_filename = 'C:/Users/lenovo/Desktop/ziliao/lizhihui/templates/home_application/home.html'
_template_uri = '/home_application/home.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/site.js" type="text/javascript"></script>\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/home.js" type="text/javascript"></script>\n\n<!--\u56fe\u8868\u63a7\u4ef6-->\n<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/plug-in/highcharts/highcharts.js"></script>\n<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/plug-in/highcharts/highcharts-3d.js"></script>\n<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/plug-in/highcharts/exporting.js"></script>\n<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/plug-in/highcharts/highcharts-more.js"></script>\n<script type="text/javascript" src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'js/plug-in/highcharts/solid-gauge.js"></script>\n\n<script src="')
        __M_writer(unicode(STATIC_URL))
        __M_writer(u'client/controllers/hostInfo.js" type="text/javascript"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 4, "35": 4, "36": 5, "37": 5, "38": 8, "39": 8, "40": 9, "41": 9, "42": 10, "43": 10, "44": 11, "45": 11, "46": 12, "47": 12, "48": 14, "49": 14, "55": 49, "27": 0}, "uri": "/home_application/home.html", "filename": "C:/Users/lenovo/Desktop/ziliao/lizhihui/templates/home_application/home.html"}
__M_END_METADATA
"""
