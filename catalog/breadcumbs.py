__author__ = 'frank'
from mycatalog.catalog.models import ItemCategory


def breadcrumbs(url):
    cats = url.split('/')[:-1]
    print(cats)
    links = []
    for cat in cats:
        item = ItemCategory.objects.filter(slug=cat)[0]
        # print(item)
        link = [
            item.name,
            u'/{}'.format(item.get_absolute_url())
        ]
        links.append(link)

    print(links)
    return links