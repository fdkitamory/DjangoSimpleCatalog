# -*- coding: utf-8 -*-
__author__ = 'frank'
from mycatalog.catalog.models import ItemCategory
from mycatalog.catalog.category_utils import cat_tree_build, cat_tree_smooth


def menu_processor(request):
    return {'categories': cat_tree_smooth(cat_tree_build(ItemCategory.objects.filter(parent__isnull=True)))}