# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^$', 'categories'),
    url(r'^(?P<url>((?:[\w-]+/){1,3}))$', 'categories'),
    # url(r'^category/$', 'categories'),
)