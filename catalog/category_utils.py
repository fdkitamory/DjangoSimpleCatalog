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


def get_cat_in_url(url):
    """Получаем обратный список категорий из урла"""
    categories = ItemCategory.objects.all()
    url = url.split('/')
    cats_in_url = []

    for cat_in_url in url[::-1]:
        for category in categories:
            if category.slug == cat_in_url:
                if not cats_in_url:
                    cats_in_url.append(category)
                elif cats_in_url[-1].parent == category:
                    cats_in_url.append(category)
                else:
                    return u'your lin shiiit!'

    return cats_in_url


















