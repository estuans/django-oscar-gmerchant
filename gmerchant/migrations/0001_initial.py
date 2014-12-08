# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'APIServiceCredentials'
        db.create_table(u'gmerchant_apiservicecredentials', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('client_id', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('client_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('private_key_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('private_key_ciphertext', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('private_key_phrase', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'gmerchant', ['APIServiceCredentials'])

        # Adding model 'GoogleMerchantAccount'
        db.create_table(u'gmerchant_googlemerchantaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('account_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('credentials', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gmerchant.APIServiceCredentials'], null=True, blank=True)),
            ('catalogue_imported', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'gmerchant', ['GoogleMerchantAccount'])


    def backwards(self, orm):
        # Deleting model 'APIServiceCredentials'
        db.delete_table(u'gmerchant_apiservicecredentials')

        # Deleting model 'GoogleMerchantAccount'
        db.delete_table(u'gmerchant_googlemerchantaccount')


    models = {
        u'gmerchant.apiservicecredentials': {
            'Meta': {'object_name': 'APIServiceCredentials'},
            'application_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'client_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private_key_ciphertext': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'private_key_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'private_key_phrase': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'gmerchant.googlemerchantaccount': {
            'Meta': {'object_name': 'GoogleMerchantAccount'},
            'account_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'account_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'catalogue_imported': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'credentials': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gmerchant.APIServiceCredentials']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['gmerchant']