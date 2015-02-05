# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth, get_cat_in_url
from pprint import pprint


def index(request):
    """Главная"""
    items = Item.objects.all()
    categories = ItemCategory.objects.filter(parent__isnull=True)
    categories = cat_tree_build(categories)
    # pprint(cat_tree_smooth(categories))

    template = loader.get_template('index.html')
    context = Context({
        'items': items,
        'categories': cat_tree_smooth(categories),
    })
    return HttpResponse(template.render(context))


def categories(request, url):
    """Вывод категорий"""
    # items = Item.objects.filter(category__slug=category)
    # print cat_three_build(categories)
    cat_in_url = get_cat_in_url(url)

    # pprint(url)
    tpl = loader.get_template('categories.html')
    c = Context({'items': url})
    return HttpResponse(tpl._render(c))