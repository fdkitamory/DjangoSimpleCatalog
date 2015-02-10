# -*- coding: utf-8 -*-
__author__ = 'frank'

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
    """Получаем обратный список категорий из урла
       Не нравится что БД дергается каждый раз, переписать через построение дерева выше"""
    categories = ItemCategory.objects.all()
    url = url.split('/')
    url = url[-2::-1]
    cats_in_url = []

    for slug in url:
        if categories.filter(slug=slug):
            category = categories.filter(slug=slug)[0]
            if not cats_in_url:
                cats_in_url.append(category)
            elif category == cats_in_url[-1].parent:
                cats_in_url.append(category)
            else:
                return False
        else:
            return False

    return cats_in_url


def cat_childs(cat):
    """Получаем чайлдов полученой категории"""
    childs = []
    childs.extend(cat.child.all())
    for child in childs:
        childs.extend(child.child.all())
        cat_childs(child)

    return childs


def cat_menu():
    return cat_tree_smooth(cat_tree_build(ItemCategory.objects.filter(parent__isnull=True)))

















