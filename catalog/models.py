# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from pytils import translit


class ItemCategory(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')
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
    slug = models.SlugField(blank=True, null=True)

    class Meta():
        ordering = ['title']

    def __unicode__(self):
        return u'#{}: {}'.format(self.pk, self.title)

    # @permalink
    # def get_absolute_url(self):
    #     return 'item_detail', None, {'object_id': self.id}

    @staticmethod
    def pre_save(sender, instance, **kwargs):
        slug = translit.slugify(u'{}-{}'.format(instance.title, instance.pk))
        if instance.slug != slug:
            instance.slug = slug
            instance.save()

signals.pre_save.connect(Item.pre_save, sender=Item)