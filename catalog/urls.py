# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    url(r'^$', 'categories'),
    url(r'^(?P<url>[\w+-]+/)$', 'categories'), #Категории первого уровня
    url(r'^(?P<url>[\w+-]+/[\w+-]+/)$', 'categories'), #Категории второго уровня
    url(r'^(?P<url>[\w+-]+/[\w+-]+/[\w+-]+/)$', 'categories'), #Категории третьего уровня уровня


    # url(r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',


    # url(r'^(?P<url_item>((?:[\w-]+/){1,3}(?:[\w-]+/)))$', 'item'), Рабочие URL
    # url(r'^(?P<url>((?:[\w-]+/){1,3}))$', 'categories'), Особенно это он для категорий


    # url(r'^category/$', 'categories'),
)