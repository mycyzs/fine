# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from home_application.mysql_cmdb_views import *



import sys
reload(sys)
sys.setdefaultencoding('utf8')


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/js_factory.html')

