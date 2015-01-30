# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from django.http import HttpRequest
from mycatalog.catalog.models import Item, ItemCategory


def index(request):
    items = Item.objects.all()
    t = loader.get_template("categories.html")
    c = Context({'items': items})
    return HttpResponse(t.render(c))


def categories(reguest, category_name):
    categories = ItemCategory.objects.filter(parent__isnull=True)
    catThree = []

    def catThreeBuild(cats):
        catBranch = {}
        for cat in cats:
            catBranch['cat'] = cat
            catBranch['sub'] = cat.child.all()

            catThreeBuild(catBranch['sub'])

        return catBranch

    for cat in categories:
        catThree.append(catThreeBuild(categories))

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

    print catThree
    # items = categories.Item.objects.all()
    tpl = loader.get_template('categories.html')
    c = Context({'categories': categories})
    return HttpResponse(tpl._render(c))

