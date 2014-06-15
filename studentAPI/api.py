from tastypie.resources import ModelResource
from tastypie import fields

from studentAPI.models import Candidate, Department
from studentAPI.models import StudentQualification, StudentAppliedDepartments


class DepartmentResource(ModelResource):
    """
    Department Resource which is independent
    """
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'department'


class StudentAppliedDepartmentsResource(ModelResource):
    """
    Returns the Departments which the student applied for. There
    is a One to One relationship with the department entity
    """
    department = fields.ToOneField(
        DepartmentResource,
        attribute='department', related_name='applied_departments',
        null=True, blank=True, full=True)

    class Meta:
        queryset = StudentAppliedDepartments.objects.all()
        resource_name = 'applied_departments'


class StudentQualificationResource(ModelResource):
    """
    Returns the qualifications for Students
    """
    class Meta:
        queryset = StudentQualification.objects.all()
        resource_name = 'qualifications'


class CandidateResource(ModelResource):
    """
    Returns the main candidate object along with the departments and
    qualifications
    """
    departments = fields.ToManyField(
        'studentAPI.api.StudentAppliedDepartmentsResource',
        'applied_departments_candidate',
        null=True, blank=True, full=True)

    qualifications = fields.ToManyField(
        'studentAPI.api.StudentQualificationResource',
        'qualifications',
        null=True, blank=True, full=True)

    class Meta:
        queryset = Candidate.objects.all()
        resource_name = 'candidate'
