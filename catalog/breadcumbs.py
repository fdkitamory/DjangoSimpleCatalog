__author__ = 'frank'
from mycatalog.catalog.models import Item, ItemCategory


def breadcrumbs(request):
    cats = request.get_full_path().strip('/').split('/')
    links = []
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
    return links