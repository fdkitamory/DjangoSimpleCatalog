# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import cat_lvl, cat_three_build


def index(request):
    """Главная"""
    items = Item.objects.all()

    categories = ItemCategory.objects.all()

    template = loader.get_template('index.html')
    context = Context({
        'items': items,
        'categories': categories
    })
    return HttpResponse(template.render(context))


def categories(request, category_name):
    """Вывод категорий"""
    categories = ItemCategory.objects.filter(parent__isnull=True)

    print cat_three_build(categories)
    tpl = loader.get_template('menu.html')
    c = Context({'categories': categories})
    return HttpResponse(tpl._render(c))