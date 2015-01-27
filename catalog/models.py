# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class GoodsCategories(models.Model):
    category = models.CharField(max_length=50)

    def __unicode__(self):
        return u'#{0}: {1}'.format(self.pk, self.category)


class GoodsCategoriesAdmin(admin.ModelAdmin):
    list_display = ("pk", "category",)


class Goods(models.Model):
    goods_title = models.CharField(max_length=150)
    goods_body = models.TextField()
    goods_category = models.ForeignKey(GoodsCategories)

    class Meta():
        ordering = ("goods_title",)


class GoodsAdmin(admin.ModelAdmin):
    """ Четкий вывод в админке >_< """

    list_display = ("goods_title", "goods_body")


# Регистрация моделей в джанго админке

admin.site.register(GoodsCategories, GoodsCategoriesAdmin)
admin.site.register(Goods, GoodsAdmin)
