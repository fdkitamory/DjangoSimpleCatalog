# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.category'
        db.add_column('catalog_item', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalog.ItemCategory'], null=True),
                      keep_default=False)

        # Removing M2M table for field category on 'Item'
        db.delete_table(db.shorten_name('catalog_item_category'))


    def backwards(self, orm):
        # Deleting field 'Item.category'
        db.delete_column('catalog_item', 'category_id')

        # Adding M2M table for field category on 'Item'
        m2m_table_name = db.shorten_name('catalog_item_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['catalog.item'], null=False)),
            ('itemcategory', models.ForeignKey(orm['catalog.itemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'itemcategory_id'])


    models = {
        'catalog.item': {
            'Meta': {'ordering': "['title']", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['catalog.ItemCategory']", 'null': 'True'}),
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