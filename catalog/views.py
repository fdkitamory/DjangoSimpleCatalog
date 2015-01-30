# -*- coding: utf-8 -*-
# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Item, ItemCategory



def index(request):
    items = Item.objects.all()
    t = loader.get_template("categories.html")
    c = Context({'items': items})
    return HttpResponse(t.render(c))


def categories(reguest, category_name):
    categories = ItemCategory.objects.filter(parent__isnull=True)
    cat_three = []

    def cat_lvl(cat, depth=0):
        return cat.parent and cat_lvl(cat.parent, depth+1) or depth

        # if cat.parent:
        #     return cat_lvl(cat.parent, depth+1)
        # return depth

    def cat_three_build(cats):

        cat_branch = {}
        for cat in cats:
            cat_branch['cat'] = cat
            cat_branch['lvl'] = cat_lvl(cat)
            cat_branch['sub'] = cat.child.all()

            cat_three_build(cat_branch['sub'])
            cat_three.append(cat_branch)

        return cat_three


    # catThree.append()

    #Bebug @_@
    # indexCategories = []
    # for category in categories:
    #     if category.parent is None:
    #         indexCategories.append(category)
    #         childCategories = []
    #         for child in category.child.all():
    #             childCategories.append(child)
    #
    #         indexCategories.append(childCategories)

    print cat_three_build(categories)
    # items = categories.Item.objects.all()
    tpl = loader.get_template('categories.html')
    c = Context({'categories': categories})
    return HttpResponse(tpl._render(c))

