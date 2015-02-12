# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from pytils import translit


class ItemCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img')
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=100)

    class Meta():
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return u'{}({})'.format(self.name, self.parent)

    @staticmethod
    def post_save(sender, instance, **kwargs):
        slug = slugify(translit.translify(u'{}_{}'.format(instance.name, instance.pk)))

        if instance.slug != slug:
            instance.slug = slug
            instance.save()

    def _get_absolute_url(self):
        return [self.slug] + (self.parent._get_absolute_url() if self.parent else [])

    def get_absolute_url(self):
        return '/'.join(reversed(self._get_absolute_url()))


class Item(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img', null=True, blank=True)
    category = models.ForeignKey(ItemCategory, null=True, related_name='item')
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=100)

    class Meta():
        ordering = ['title']

    def __unicode__(self):
        return u'#{}: {}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return u'{}/{}/'.format(ItemCategory.get_absolute_url(self.category), self.slug)

    @staticmethod
    def post_save(sender, instance, **kwargs):
        slug = slugify(translit.translify(u'item_{}_{}'.format(instance.title, instance.pk)))

        if instance.slug != slug:
                instance.slug = slug
                instance.save()


signals.post_save.connect(Item.post_save, sender=Item)
signals.post_save.connect(ItemCategory.post_save, sender=ItemCategory)