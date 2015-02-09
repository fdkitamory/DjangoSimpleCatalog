# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import *
from pprint import pprint
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


def index(request):
    """Главная"""
    items = Item.objects.all()
    categories = ItemCategory.objects.filter(parent__isnull=True)
    categories = cat_tree_build(categories)
    # pprint(cat_tree_smooth(categories))

    return render_to_response('index.html', {
        'items': items,
        'categories': cat_tree_smooth(categories),
    })


def categories(request, url):
    """Вывод категорий"""
    cat_in_url = get_cat_in_url(url)[0]
    item_err = 'Эээ, сорян категория пуста'
    items = []
    if cat_in_url is False:
        raise Http404
    else:
        cats = [cat_in_url]
        cats.extend(cat_childs(cat_in_url))

        for cat in cats:
            items.extend(cat.item.all())

    for item in items:
        if not item.image:
            item.image = item.category.image

    categories = ItemCategory.objects.filter(parent__isnull=True)
    categories = cat_tree_build(categories)

    if not items:
        return render_to_response('categories.html', {
            'item': item_err,
            'categories': cat_tree_smooth(categories),
        })
    else:
        return render_to_response('categories.html', {
            'items': items,
            'categories': cat_tree_smooth(categories),
        })


def item(request, url):
    item = url.split('/')[-2:1:-1][0]
    cats = url.split('/')[-3::-1]

    item = Item.objects.filter(slug=item)[0]

    if not item.image:
        item.image = item.category.image

    pprint(item)
    categories = ItemCategory.objects.filter(parent__isnull=True)
    categories = cat_tree_build(categories)
    context = Context({
        'item': item,
        'categories': cat_tree_smooth(categories),
    })

    return render_to_response('item.html', {
        'items': items,
        'categories': cat_tree_smooth(categories),
    })

































