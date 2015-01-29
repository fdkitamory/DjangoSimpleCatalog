__author__ = 'frank'

from catalog.models import *
from django.contrib import admin


class ItemCategoryAdm(admin.ModelAdmin):
    list_display = ('name', 'parent', 'image')


class ItemAdm(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(ItemCategory, ItemCategoryAdm)
admin.site.register(Item, ItemAdm)