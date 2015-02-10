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
    print(request.get_full_path())
    return render_to_response('index.html', {
        'items': page_pagination(request, items, 12),
        'categories': cat_menu(),
    })


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
        'categories': cat_menu()
    }

    if not items:
        context['item_err'] = 'Эээ, сорян категория пуста'
    else:
        context['items'] = page_pagination(request, items, 12)

    return render_to_response('categories.html', context)


def item_page(request, url):
    item = url.split('/')[-2:1:-1][0]
    # cats = url.split('/')[-3::-1]

    # print(url)
    item = Item.objects.filter(slug=item)[0]

    return render_to_response('item.html', {
        'links': breadcrumbs(url),
        'item': item,
        'categories': cat_menu(),
    })


def search_page(request):

    if request.method == 'POST':
        form_search = SearchForm(request.POST)
        if form_search.is_valid():
            return render_to_response('search.html', {'hello': 'Hello World! I`m search! :)'})
    else:
        form_search = SearchForm()

    context = {
        'form_search': form_search,
    }
    # context = {
    #     'form_search': 'Hello World!',
    # }

    return render_to_response('search.html', context)











# def contact(request):
#     if request.method == 'POST': # If the form has been submitted...
#         form = ContactForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             # Process the data in form.cleaned_data
#             # ...
#             return HttpResponseRedirect('/thanks/') # Redirect after POST
#     else:
#         form = ContactForm() # An unbound form
#
#     return render_to_response('contact.html', {
#         'form': form,
#     })



















