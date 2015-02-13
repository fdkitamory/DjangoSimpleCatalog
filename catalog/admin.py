__author__ = 'frank'

from catalog.models import ItemCategory, Item
from django.contrib import admin


class ItemCategoryAdm(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'image')


class ItemAdm(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'image')

admin.site.register(ItemCategory, ItemCategoryAdm)
admin.site.register(Item, ItemAdm)