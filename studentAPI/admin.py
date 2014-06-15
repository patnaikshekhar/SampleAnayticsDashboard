from django.contrib import admin
from studentAPI.models import Candidate, Department
from studentAPI.models import StudentQualification, StudentAppliedDepartments


class StudentQualificationInline(admin.StackedInline):
    """
        Inline class for Qualifications
    """

    model = StudentQualification
    extra = 3


class StudentAppliedDepartments(admin.StackedInline):
    """
        Inline class for Applied Departments
    """

    model = StudentAppliedDepartments
    extra = 3


class CandidateAdmin(admin.ModelAdmin):
    """
        Main Candidate class to show on the model. Used to define
        the inlines for easy data entry
    """

    inlines = [StudentQualificationInline, StudentAppliedDepartments]

# Register the Candidate Model
admin.site.register(Candidate, CandidateAdmin)

# Register the Department Model
admin.site.register(Department)
