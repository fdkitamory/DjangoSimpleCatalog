# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', 'index', name='index'),
    # url(r'^$', 'categories'),
    url(r'^(?P<url>([\w/-]+)/item_([\w+-])+/)$', 'item'), #Конкретный товар
    url(r'^(?P<url>([\w-]+/){1,3})$', 'categories'), #Категории

    # url(r'^(?P<url_item>((?:[\w-]+/){1,3}(?:[\w-]+/)))$', 'item'), Рабочие URL
    # url(r'^(?P<url>((?:[\w-]+/){1,3}))$', 'categories'), Особенно это он для категорий


    # url(r'^category/$', 'categories'),
)