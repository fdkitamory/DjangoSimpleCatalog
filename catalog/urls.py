# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
# from mycatalog.catalog.views import index, categories

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^$', 'categories'),
    url(r'^(?P<category>((?:[\w-]+/){1,3}))$', 'categories'),
    # url(r'^category/$', 'categories'),
)