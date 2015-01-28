# -*- coding: utf-8 -*-
from django.db import models
#from django.db.models import permalink
from django.contrib import admin


class ItemCategory(models.Model):
    parent = models.ForeignKey('self', null=True, related_name='child')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta():
        ordering = ['name']
        verbose_name_plural = 'Categories'


class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    category = models.ManyToManyField(ItemCategory, blank=True)

    class Meta():
        ordering = ['title']

    # @permalink
    # def get_absolute_url(self):
    #     return 'item_detail', None, {'object_id': self.id}


class ItemCategoryAdm(admin.ModelAdmin):
    list_display = ('name', 'parent', 'image')


class ItemAdm(admin.ModelAdmin):
    list_display = ('title', 'image',)


admin.site.register(ItemCategory, ItemCategoryAdm)
admin.site.register(Item, ItemAdm)
