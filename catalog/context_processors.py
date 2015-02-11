# -*- coding: utf-8 -*-
__author__ = 'frank'
from mycatalog.catalog.models import ItemCategory, Item
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth
from mycatalog.catalog.search import SearchForm
from django.core.context_processors import csrf


def menu_processor(request):
    return {'categories': cat_tree_smooth(cat_tree_build(ItemCategory.objects.filter(parent__isnull=True)))}


def breadcrumbs_processor(request):
    cats = request.get_full_path().strip('/').split('/')
    links = []
    if cats[0] and cats[0] != u'search':
        try:
            for cat in cats:
                if ItemCategory.objects.filter(slug=cat):
                    item = ItemCategory.objects.filter(slug=cat)[0]
                    title = item.name
                else:
                    item = Item.objects.filter(slug=cat)[0]
                    title = item.title

                link = {
                    'link': u'/{}'.format(item.get_absolute_url()),
                    'title': title
                }

                links.append(link)

        except IndexError:
            links = []

    elif cats[0] == u'search':
        links = [u'Поиск']

    return {'links': links}


def search_processor(request):
    return {'form_search': SearchForm()}


def csrf_token_processor(request):
    return {'csrf_token': csrf(request)}
