# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from pytils import translit
from catalog.supprots import stringCodesSum
from random import randint


class ItemCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta():
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return u'{0}'.format(self.name)

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        slug = slugify(translit.translify(u'{}'.format(instance.name)))

        if ItemCategory.objects.filter(slug=slug) is not None or instance.slug is None:
            slug = u'{}_{}'.format(slug, stringCodesSum(u'{}{}'.format(slug, randint(1, 10000))))

            if instance.slug != slug:
                instance.slug = slug
                instance.save()
        else:
            if instance.slug != slug:
                instance.slug = slug
                instance.save()


class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    category = models.ForeignKey(ItemCategory, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class Meta():
        ordering = ['title']

    def __unicode__(self):
        return u'#{}: {}'.format(self.pk, self.title)

    # @permalink
    # def get_absolute_url(self):
    #     return 'item_detail', None, {'object_id': self.id}

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        slug = slugify(translit.translify(u'{}_{}'.format(instance.title, instance.pk)))

        if ItemCategory.objects.filter(slug=slug) is not None or instance.slug is None:
            slug = u'{}_{}'.format(slug, stringCodesSum(u'{}{}'.format(slug, randint(1, 1000))))

            if instance.slug != slug:
                instance.slug = slug
                instance.save()
        else:
            if instance.slug != slug:
                instance.slug = slug
                instance.save()

signals.pre_save.connect(Item.pre_save, sender=Item)
signals.pre_save.connect(ItemCategory.pre_save, sender=ItemCategory)