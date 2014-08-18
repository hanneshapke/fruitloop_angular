# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FruitType'
        db.create_table(u'fruit_fruittype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'fruit', ['FruitType'])


        # Renaming column for 'FruitLocation.fruit_type' to match new field type.
        db.rename_column(u'fruit_fruitlocation', 'fruit_type', 'fruit_type_id')
        # Changing field 'FruitLocation.fruit_type'
        db.alter_column(u'fruit_fruitlocation', 'fruit_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fruit.FruitType']))
        # Adding index on 'FruitLocation', fields ['fruit_type']
        db.create_index(u'fruit_fruitlocation', ['fruit_type_id'])


    def backwards(self, orm):
        # Removing index on 'FruitLocation', fields ['fruit_type']
        db.delete_index(u'fruit_fruitlocation', ['fruit_type_id'])

        # Deleting model 'FruitType'
        db.delete_table(u'fruit_fruittype')


        # Renaming column for 'FruitLocation.fruit_type' to match new field type.
        db.rename_column(u'fruit_fruitlocation', 'fruit_type_id', 'fruit_type')
        # Changing field 'FruitLocation.fruit_type'
        db.alter_column(u'fruit_fruitlocation', 'fruit_type', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        u'fruit.fruitlocation': {
            'Meta': {'ordering': "['-modified']", 'object_name': 'FruitLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fruit_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fruit.FruitType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'fruit.fruittype': {
            'Meta': {'ordering': "['-modified']", 'object_name': 'FruitType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['fruit']