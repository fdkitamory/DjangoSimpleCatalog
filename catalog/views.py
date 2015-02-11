# -*- coding: utf-8 -*-
# Create your views here.

from mycatalog.catalog.models import Item
from mycatalog.catalog.category_utils import cat_childs, get_cat_in_url
from mycatalog.catalog.pagination import page_pagination
from mycatalog.catalog.breadcumbs import breadcrumbs
from mycatalog.catalog.search import SearchForm
from pprint import pprint
from django.http import Http404
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext


def index(request):
    """Главная"""
    items = Item.objects.all()
    context = {
        'items': page_pagination(request, items, 12)
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def categories_page(request, url):
    """Вывод категорий"""

    if get_cat_in_url(url)[0] is False:
        raise Http404
    else:
        items = []
        cats = get_cat_in_url(url)
        cats.extend(cat_childs(cats[0]))

        for cat in cats:
            items.extend(cat.item.all())

    context = {
        'items': page_pagination(request, items, 12),
        'item_err': 'Эээ, сорян категория пуста'
    }
    return render_to_response('categories.html', context)


def item_page(request, url):
    item = url.strip('/').split('/')[-1]
    item = Item.objects.filter(slug=item)[0]
    return render_to_response('item.html', {
        'item': item
    }, context_instance=RequestContext(request))


def search_page(request):
    items = []
    if request.method == 'GET':
        form_search = SearchForm(request.GET)
        if form_search.is_valid():
            items = Item.objects.filter(title__contains=request.GET['q'])
    else:
        form_search = SearchForm()

    context = {
        'form_search': form_search,
        'items': page_pagination(request, items, 12),
        'item_err': 'Нет результата или указана пустая строка, попробуйте ещё раз',
        'search_query': u'q={}&'.format(request.GET['q'])
    }
    return render_to_response('search_page.html', context, context_instance=RequestContext(request))



















