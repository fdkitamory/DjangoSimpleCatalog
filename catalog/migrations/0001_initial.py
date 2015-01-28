# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemCategory'
        db.create_table('catalog_itemcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='child', null=True, to=orm['catalog.ItemCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('catalog', ['ItemCategory'])

        # Adding model 'Item'
        db.create_table('catalog_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('catalog', ['Item'])

        # Adding M2M table for field category on 'Item'
        m2m_table_name = db.shorten_name('catalog_item_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['catalog.item'], null=False)),
            ('itemcategory', models.ForeignKey(orm['catalog.itemcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['item_id', 'itemcategory_id'])


    def backwards(self, orm):
        # Deleting model 'ItemCategory'
        db.delete_table('catalog_itemcategory')

        # Deleting model 'Item'
        db.delete_table('catalog_item')

        # Removing M2M table for field category on 'Item'
        db.delete_table(db.shorten_name('catalog_item_category'))


    models = {
        'catalog.item': {
            'Meta': {'ordering': "['title']", 'object_name': 'Item'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['catalog.ItemCategory']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'catalog.itemcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'ItemCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'child'", 'null': 'True', 'to': "orm['catalog.ItemCategory']"})
        }
    }

    complete_apps = ['catalog']