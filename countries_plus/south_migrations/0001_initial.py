# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('countries_plus_country', (
            ('iso', self.gf('django.db.models.fields.CharField')(primary_key=True, max_length=2)),
            ('iso3', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('iso_numeric', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('fips', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('capital', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('area', self.gf('django.db.models.fields.DecimalField')(max_digits=11, blank=True, decimal_places=2, null=True)),
            ('population', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('continent', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=2)),
            ('tld', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('currency_code', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=3)),
            ('currency_symbol', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('currency_name', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('postal_code_format', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('postal_code_regex', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('languages', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('geonameid', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('neighbours', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=255)),
            ('equivalent_fips_code', self.gf('django.db.models.fields.CharField')(blank=True, null=True, max_length=4)),
        ))
        db.send_create_signal('countries_plus', ['Country'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('countries_plus_country')


    models = {
        'countries_plus.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'area': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'blank': 'True', 'decimal_places': '2', 'null': 'True'}),
            'capital': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'continent': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '2'}),
            'currency_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'currency_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'currency_symbol': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'equivalent_fips_code': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '4'}),
            'fips': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '3'}),
            'geonameid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'iso_numeric': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'neighbours': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'population': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'postal_code_format': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'postal_code_regex': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'tld': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['countries_plus']