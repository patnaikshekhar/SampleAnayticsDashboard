import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admissions.settings")
from django.conf import settings

from studentAPI.models import Department, Candidate
from studentAPI.models import StudentQualification, StudentAppliedDepartments


def clearData():
    Department.objects.all().delete()
    Candidate.objects.all().delete()


def createDepartments():
    json_data = open('sample_data/departments.json')
    data = json.load(json_data)

    for department in data:
        d = Department()
        d.name = department['name']
        d.description = department['description']
        d.save()


def createCandidates():
    json_data = open('sample_data/candidates.json')
    data = json.load(json_data)

    for candidate in data:
        c = Candidate()

        c.first_name = candidate['first_name']
        c.last_name = candidate['last_name']
        c.gender = candidate['gender']
        c.admission_year = candidate['admission_year']
        c.date_of_birth = candidate['date_of_birth']
        c.email = candidate['email']

        c.nationality = candidate['nationality']
        c.ethnicity = candidate['ethnicity']

        c.address_line_1 = candidate['address_line_1']
        c.city = candidate['city']
        c.state = candidate['state']
        c.zip_code = candidate['zip_code']
        c.country = candidate['country']
        c.save()

        for qual in candidate['qualifications']:
            q = StudentQualification()
            q.candidate = c
            q.name = qual['name']
            q.university = qual['university']
            q.year = qual['year']
            q.score = qual['score']
            q.GPA = qual['GPA']
            q.save()

        for dept in candidate['departments']:
            department = Department.objects.get(name=dept)
            d = StudentAppliedDepartments()
            d.department = department
            d.candidate = c
            d.save()


if __name__ == '__main__':
    clearData()
    createDepartments()
    createCandidates()
