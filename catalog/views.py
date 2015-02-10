# -*- coding: utf-8 -*-
# Create your views here.

from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import *
from mycatalog.catalog.pagination import page_pagination
from mycatalog.catalog.breadcumbs import breadcrumbs
from mycatalog.catalog.search import SearchForm
from pprint import pprint
from django.http import Http404

from django.shortcuts import render_to_response
from django.core.context_processors import csrf


def index(request):
    """Главная"""
    items = Item.objects.all()
    context = {
        'items': page_pagination(request, items, 12),
        'categories': cat_menu(),
        'form_search': SearchForm()
    }
    context.update(csrf(request))
    return render_to_response('index.html', context)


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
        'links': breadcrumbs(url),
        'categories': cat_menu(),
        'items': page_pagination(request, items, 12),
        'item_err': 'Эээ, сорян категория пуста',
        'form_search': SearchForm()
    }
    context.update(csrf(request))
    return render_to_response('categories.html', context)


def item_page(request, url):
    item = url.split('/')[-2:1:-1][0]
    item = Item.objects.filter(slug=item)[0]
    return render_to_response('item.html', {
        'links': breadcrumbs(url),
        'item': item,
        'categories': cat_menu(),
    })


def search_page(request):
    items = []

    if request.method == 'POST':
        form_search = SearchForm(request.POST)
        if form_search.is_valid():
            items = Item.objects.filter(title__contains=request.POST['query'])
    elif request.method == 'GET':
        form_search = SearchForm(request.GET)
        if form_search.is_valid():
            items = Item.objects.filter(title__contains=request.GET['query'])
    else:
        form_search = SearchForm()

    context = {
        'form_search': form_search,
        'links': ['Поиск'],
        'categories': cat_menu(),
        'items': items,
        'item_err': 'Нет результата или указана пустая строка, попробуйте ещё раз'
    }
    context.update(csrf(request))
    return render_to_response('search_page.html', context)



















