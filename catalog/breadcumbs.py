__author__ = 'frank'
from mycatalog.catalog.models import ItemCategory


def breadcrumbs(url):
    cats = url.split('/')[:-1]
    links = []
    for cat in cats:
        item = ItemCategory.objects.filter(slug=cat)[0]
        link = [
            item.name,
            u'/{}'.format(item.get_absolute_url())
        ]
        links.append(link)
    return links