

from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

def generate_unique_id(user_type):
        current_year = datetime.datetime.now().year
        unique_id = uuid.uuid4().hex[:8].upper()  # Generate a unique 8-character hex string
        return f'{current_year}-{user_type.upper()}-{unique_id}'

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
    
   

    def save(self, *args, **kwargs):
        if not self.dord_number:
            self.dord_number = generate_unique_id(self.user_type)
        super(UserRegistration, self).save(*args, **kwargs)



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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bookmarked_projects = models.ManyToManyField(Project_store, blank=True, related_name='bookmarked_by')

    def __str__(self):
        return self.user.username

# Ensure that each user has a UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class ProjectApplication(models.Model):
    project = models.ForeignKey(Project_store, on_delete=models.CASCADE)
    user_details = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    remarks=models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"

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














