# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
# from mycatalog.catalog.views import index, categories

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^$', 'categories'),
    url(r'^(?P<category_name>)[\w -_]+/$', 'categories'),
    url(r'^category/$', 'categories'),
)