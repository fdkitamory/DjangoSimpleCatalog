__author__ = 'frank'
from mycatalog.catalog.models import ItemCategory
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth
from mycatalog.catalog.breadcumbs import breadcrumbs


def menu_processor(request):
    return {'categories': cat_tree_smooth(cat_tree_build(ItemCategory.objects.filter(parent__isnull=True)))}


def breadcrumbs_processor(requst, url):
    return {'links': breadcrumbs(url)}