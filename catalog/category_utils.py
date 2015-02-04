# -*- coding: utf-8 -*-
__author__ = 'frank'

# from pytils import translit
# from pprint import pprint
from mycatalog.catalog.models import ItemCategory

def cat_lvl(cat, depth=0):
    """Считаем вложеность категорий"""
    return cat.parent and cat_lvl(cat.parent, depth+1) or depth


def cat_tree_build(cats):
    """Строим дерево категорий"""
    cat_tree = []

    for cat in cats:
        cat_branch = {
            'cat': cat,
            'lvl': cat_lvl(cat),
            'sub': cat.child.all()
        }
        cat_branch['sub'] = cat_tree_build(cat_branch['sub'])
        cat_tree.append(cat_branch)

    return cat_tree


def cat_tree_smooth(cats):
    """Размазываем в удобочитаемый вид это же дерево"""
    cat_list = []
    for cat in cats:
        cat_list_item = {
            'lvl': cat['lvl'] * 10,
            'name': cat['cat'].name,
            'slug': ItemCategory.get_absolute_url(cat['cat'])
        }
        cat_list.append(cat_list_item)
        cat_list.extend(cat_tree_smooth(cat['sub']))

    return cat_list