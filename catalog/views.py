# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth, get_cat_in_url
from pprint import pprint
from django.http import Http404


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
    cat_in_url = get_cat_in_url(url)

    if cat_in_url is False:
        raise Http404
    else:
        for cat in cat_in_url:

        items = Item.objects.filter(category__slug=cat_in_url[0])

    pprint(cat_in_url)
    tpl = loader.get_template('categories.html')
    c = Context({'items': items})
    return HttpResponse(tpl._render(c))