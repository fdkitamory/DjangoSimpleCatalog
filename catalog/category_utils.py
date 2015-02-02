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
        cat_list_item = []
        cat_list_item.append(u'{}'.format(cat['lvl']))
        cat_list_item.append(u'{}'.format(translit.translify(cat['cat'].name)))
        cat_list_item.append(u'{}'.format(cat['cat'].slug))
        cat_list.append(cat_list_item)
        cat_list.extend(cat_tree_smooth(cat['sub']))

    return cat_list



# [{'cat': <ItemCategory: Мониторы>,
#   'lvl': 0,
#   'sub': [{'cat': <ItemCategory: benq>,
#            'lvl': 1,
#            'sub': [{'cat': <ItemCategory: 18.5 inch>, 'lvl': 2, 'sub': []},
#                    {'cat': <ItemCategory: 21.5 inch>, 'lvl': 2, 'sub': []}]},
#           {'cat': <ItemCategory: Самсунг>,
#            'lvl': 1,
#            'sub': [{'cat': <ItemCategory: 18.5 inch>, 'lvl': 2, 'sub': []},
#                    {'cat': <ItemCategory: 21.5 inch>, 'lvl': 2, 'sub': []},
#                    {'cat': <ItemCategory: 24 inch>, 'lvl': 2, 'sub': []}]}]},
#  {'cat': <ItemCategory: Телевизоры>, 'lvl': 0, 'sub': []},
#  {'cat': <ItemCategory: Телефоны>,
#   'lvl': 0,
#   'sub': [{'cat': <ItemCategory: Бабушкафоны>,
#            'lvl': 1,
#            'sub': []},
#           {'cat': <ItemCategory: Смартфоны>, 'lvl': 1, 'sub': []}]}]








# [[0, 'Cat_Title', SLUG], [0, 'Cat_Title', SLUG], [0, 'Cat_Title', SLUG], [0, 'Cat_Title', SLUG]]