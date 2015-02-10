# -*- coding: utf-8 -*-
# Create your views here.

from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import *
from mycatalog.catalog.pagination import page_pagination
from mycatalog.catalog.breadcumbs import breadcrumbs
from pprint import pprint
from django.http import Http404

from django.shortcuts import render_to_response


def index(request):
    """Главная"""
    items = Item.objects.all()

    return render_to_response('index.html', {
        'items': page_pagination(request, items, 12),
        'categories': cat_menu(),
    })


def categories_page(request, url):
    """Вывод категорий"""
    items = []

    if get_cat_in_url(url)[0] is False:
        raise Http404
    else:
        cats = get_cat_in_url(url)
        cats.extend(cat_childs(cats[0]))

        for cat in cats:
            items.extend(cat.item.all())

    if not items:
        return render_to_response('categories.html', {
            'item_err': 'Эээ, сорян категория пуста',
            'categories': cat_menu(),
            'links': breadcrumbs(url)
        })
    else:
        return render_to_response('categories.html', {
            'items': page_pagination(request, items, 12),
            'categories': cat_menu(),
            'links': breadcrumbs(url)
        })


def item_page(request, url):
    item = url.split('/')[-2:1:-1][0]
    cats = url.split('/')[-3::-1]

    item = Item.objects.filter(slug=item)[0]

    category_list = ItemCategory.objects.filter(parent__isnull=True)
    category_list = cat_tree_build(category_list)

    return render_to_response('item.html', {
        'item': item,
        'categories': cat_tree_smooth(category_list),
    })

































