# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Candidate.address_line_2'
        db.add_column(u'studentAPI_candidate', 'address_line_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Candidate.address_line_2'
        db.delete_column(u'studentAPI_candidate', 'address_line_2')


    models = {
        u'studentAPI.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'admission_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fathers_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mothers_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'studentAPI.department': {
            'Meta': {'object_name': 'Department'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'studentAPI.studentapplieddepartments': {
            'Meta': {'object_name': 'StudentAppliedDepartments'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentAPI.Candidate']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentAPI.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'studentAPI.studentqualification': {
            'GPA': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'StudentQualification'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['studentAPI.Candidate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year_of_passing': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['studentAPI']