# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.image'
        db.alter_column('catalog_item', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Item.slug'
        db.alter_column('catalog_item', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True, null=True))

        # Changing field 'ItemCategory.slug'
        db.alter_column('catalog_itemcategory', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True, null=True))

    def backwards(self, orm):

        # Changing field 'Item.image'
        db.alter_column('catalog_item', 'image', self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2015, 2, 11, 0, 0), max_length=100))

        # Changing field 'Item.slug'
        db.alter_column('catalog_item', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, null=True))

        # Changing field 'ItemCategory.slug'
        db.alter_column('catalog_itemcategory', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, null=True))

    models = {
        'catalog.item': {
            'Meta': {'ordering': "['title']", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item'", 'null': 'True', 'to': "orm['catalog.ItemCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'catalog.itemcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['catalog.ItemCategory']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['catalog']