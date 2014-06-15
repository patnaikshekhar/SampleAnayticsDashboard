# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Candidate'
        db.create_table(u'studentAPI_candidate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('admission_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('fathers_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mothers_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ethnicity', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address_line_1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'studentAPI', ['Candidate'])

        # Adding model 'Department'
        db.create_table(u'studentAPI_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'studentAPI', ['Department'])

        # Adding model 'StudentQualification'
        db.create_table(u'studentAPI_studentqualification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentAPI.Candidate'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('year_of_passing', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('GPA', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'studentAPI', ['StudentQualification'])

        # Adding model 'StudentAppliedDepartments'
        db.create_table(u'studentAPI_studentapplieddepartments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentAPI.Candidate'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['studentAPI.Department'])),
        ))
        db.send_create_signal(u'studentAPI', ['StudentAppliedDepartments'])


    def backwards(self, orm):
        # Deleting model 'Candidate'
        db.delete_table(u'studentAPI_candidate')

        # Deleting model 'Department'
        db.delete_table(u'studentAPI_department')

        # Deleting model 'StudentQualification'
        db.delete_table(u'studentAPI_studentqualification')

        # Deleting model 'StudentAppliedDepartments'
        db.delete_table(u'studentAPI_studentapplieddepartments')


    models = {
        u'studentAPI.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'address_line_1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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