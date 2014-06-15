from django.db import models


class Candidate(models.Model):
    """
    This is the central candidate model which stores the applicant
    information.
    """

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    ETHNICITY_CHOICES = (
        ('H', 'Hispanic'),
        ('A', 'Asian'),
        ('AA', 'African-American'),
        ('AP', 'Asian/Pacific Islanders'),
        ('C', 'Caucasian'),
        ('O', 'Other'),
    )

    # Basic Info
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_year = models.PositiveIntegerField()
    date_of_birth = models.DateField()

    # Contact Info
    phone_number = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=50)

    # Parents Info
    fathers_name = models.CharField(max_length=200, blank=True)
    mothers_name = models.CharField(max_length=200, blank=True)

    # Demographic Info
    nationality = models.CharField(max_length=50, blank=True)
    ethnicity = models.CharField(
        max_length=1, choices=ETHNICITY_CHOICES,
        blank=True)

    # Address
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Department(models.Model):
    """
        Stores the Department information
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name


class StudentQualification(models.Model):
    """
        Stores the qualifications for each student and the scores
    """
    candidate = models.ForeignKey(Candidate, related_name='qualifications')
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year_of_passing = models.PositiveIntegerField()
    GPA = models.DecimalField(max_digits=2, decimal_places=1)


class StudentAppliedDepartments(models.Model):
    """
        Stores the Department which the student has applied for.
    """
    candidate = models.ForeignKey(
        Candidate,
        related_name='applied_departments_candidate')

    department = models.ForeignKey(
        Department,
        related_name='applied_departments')
