# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'APIServiceCredentials.client_email'
        db.alter_column(u'gmerchant_apiservicecredentials', 'client_email', self.gf('django.db.models.fields.EmailField')(max_length=128))

    def backwards(self, orm):

        # Changing field 'APIServiceCredentials.client_email'
        db.alter_column(u'gmerchant_apiservicecredentials', 'client_email', self.gf('django.db.models.fields.EmailField')(max_length=75))

    models = {
        u'gmerchant.apiservicecredentials': {
            'Meta': {'object_name': 'APIServiceCredentials'},
            'application_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'client_email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'private_key_ciphertext': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'private_key_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'private_key_phrase': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'})
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