# -*- coding: utf-8 -*-
__author__ = 'frank'


def cat_lvl(cat, depth=0):
    """Считаем вложеность категорий"""
    return cat.parent and cat_lvl(cat.parent, depth+1) or depth


def cat_three_build(cats):
    """Строим дерево категорий"""
    cat_three = []
    cat_branch = {}
    for cat in cats:
        cat_branch['cat'] = cat
        cat_branch['lvl'] = cat_lvl(cat)
        cat_branch['sub'] = cat.child.all()
        cat_three_build(cat_branch['sub'])
        cat_three.append(cat_branch)

    return cat_three