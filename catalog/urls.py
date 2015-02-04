# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
# from mycatalog.catalog.views import index, categories

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^$', 'categories'),
    # url(r'(?P<category>\w)/$', 'categories'),
    # url(r'(?P<category>[A-Za-z0-9_-]+)[/]$', 'categories'),

    # url(r'([a-zA-Z0-9_-]+)/$', 'categories'), Рабочее

    url(r'^(?P<category>((?:[\w-]+/){1,3}))$', 'categories'),


    # url(r'^([A-Za-z0-9_-]+/)|+$', 'categories'),

    url(r'^category/$', 'categories'),
)

# /^[a-z0-9-]+$/