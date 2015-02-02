# -*- coding: utf-8 -*-
__author__ = 'frank'

from pytils import translit
from pprint import pprint

def cat_lvl(cat, depth=0):
    """Считаем вложеность категорий"""
    return cat.parent and cat_lvl(cat.parent, depth+1) or depth


def cat_tree_build(cats):
    """Строим дерево категорий"""
    cat_tree = []

    for cat in cats:
        cat_branch = {}
        cat_branch['cat'] = cat
        cat_branch['lvl'] = cat_lvl(cat)
        cat_branch['sub'] = cat.child.all()
        cat_branch['sub'] = cat_tree_build(cat_branch['sub'])
        cat_tree.append(cat_branch)

    return cat_tree


def cat_tree_smooth(cats):
    cat_list = []

    for cat in cats:
        cat_list_item = {}
        cat_list_item['lvl'] = cat['lvl']
        cat_list_item['name'] = cat['cat'].name
        cat_list_item['slug']=cat['cat'].slug
        cat_list.append(cat_list_item)
        cat_list.extend(cat_tree_smooth(cat['sub']))

    return cat_list