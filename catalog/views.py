# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth
from pprint import pprint


def index(request):
    """Главная"""
    items = Item.objects.all()
    categories = ItemCategory.objects.filter(parent__isnull=True)
    categories = cat_tree_build(categories)
    pprint(cat_tree_smooth(categories))

    template = loader.get_template('index.html')
    context = Context({
        'items': items,
        'categories': cat_tree_smooth(categories),
    })
    return HttpResponse(template.render(context))


def categories(request, category_name):
    """Вывод категорий"""
    items = Item.objects.filter(category__slug=category_name)
    # print cat_three_build(categories)
    tpl = loader.get_template('categories.html')
    c = Context({'items': items})
    return HttpResponse(tpl._render(c))