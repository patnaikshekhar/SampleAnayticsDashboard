# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Candidate.ethnicity'
        db.alter_column(u'studentAPI_candidate', 'ethnicity', self.gf('django.db.models.fields.CharField')(max_length=2))

    def backwards(self, orm):

        # Changing field 'Candidate.ethnicity'
        db.alter_column(u'studentAPI_candidate', 'ethnicity', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        u'studentAPI.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address_line_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'admission_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'fathers_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'mothers_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'studentAPI.department': {
            'Meta': {'object_name': 'Department'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'studentAPI.studentapplieddepartments': {
            'Meta': {'object_name': 'StudentAppliedDepartments'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applied_departments_candidate'", 'to': u"orm['studentAPI.Candidate']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applied_departments'", 'to': u"orm['studentAPI.Department']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'studentAPI.studentqualification': {
            'GPA': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '2', 'decimal_places': '1', 'blank': 'True'}),
            'Meta': {'object_name': 'StudentQualification'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'qualifications'", 'to': u"orm['studentAPI.Candidate']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['studentAPI']