# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Item', fields ['slug']
        db.create_unique('catalog_item', ['slug'])

        # Adding field 'ItemCategory.slug'
        db.add_column('catalog_itemcategory', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'Item', fields ['slug']
        db.delete_unique('catalog_item', ['slug'])

        # Deleting field 'ItemCategory.slug'
        db.delete_column('catalog_itemcategory', 'slug')


    models = {
        'catalog.item': {
            'Meta': {'ordering': "['title']", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.ItemCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'catalog.itemcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['catalog.ItemCategory']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['catalog']