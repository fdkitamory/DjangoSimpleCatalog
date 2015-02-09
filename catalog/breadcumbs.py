__author__ = 'frank'
from mycatalog.catalog.models import Item, ItemCategory


def breadcrumbs(url):
    cats = url.split('/')[-2::-1]
    links = []
    for cat in cats:
        item = ItemCategory.objects.filter(slug=cat)[0]
        print(item)
        link = [
            item.name,
            cat
        ]
        links.append(link)
    return links