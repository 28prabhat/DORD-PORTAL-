

from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USER_TYPE_CHOICES = [
        ('admin', 'Admin (DORD)'),
        ('dean', 'Dean'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty of IITK'),
        ('researchScholar', 'Research Scholars of IITK'),
        ('sectionB', 'Section B companies'),
        ('siicCompanies', 'SIIC Incubated companies'),
        ('projectStaff', 'Project Staff'),
    ]
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    dord_number = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    firm_expertise = models.TextField(blank=True)
    sector_expertise = models.CharField(max_length=100)
    subsector_expertise = models.CharField(max_length=100, blank=True)
    past_projects = models.TextField(blank=True)
    
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    course = models.CharField(max_length=100, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Project_store(models.Model):
    title = models.CharField(max_length=200)
    supervisor = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)  # Assuming tags as comma-separated values
    country = models.CharField(max_length=50)
    open_to = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=100)
    deadline = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    serial_no = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    vacancy = models.IntegerField()
    duration = models.CharField(max_length=50)
    release_date = models.DateField()
    eligibility = models.TextField()
    expertise = models.TextField()

    def __str__(self):
        return self.title


# from django.db import models

# class Project(models.Model):
#     title = models.CharField(max_length=200)
#     serial_no = models.CharField(max_length=50)
#     department = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     description = models.TextField()
#     vacancy = models.IntegerField()
#     duration = models.CharField(max_length=50)
#     release_date = models.DateField()
#     deadline = models.DateField()
#     budget = models.DecimalField(max_digits=10, decimal_places=2)
#     eligibility = models.TextField()
#     expertise = models.TextField()

#     def __str__(self):
#         return self.title














