# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns(
    'mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^search/$', 'search_page'),
    url(r'^(?P<url>([\w/-]+)/item_([\w+-])+/)$', 'item_page'),
    url(r'^(?P<url>([\w-]+/){1,3})$', 'categories_page'),

)