# -*- coding: utf-8 -*-
__author__ = 'frank'

from django import forms


class SearchForm(forms.Form):
    """Назвал в одну букву специально для лаконичности, сократив от query"""
    q = forms.CharField(max_length=50, min_length=3)