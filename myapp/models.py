

from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid

class PastProject(models.Model):
    project_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.CharField(max_length=255)
    funding_obtained = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    grant_number = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.project_name

class Sector(models.Model):

    SECTOR_CHOICES = [
        ('agricultureNaturalResourcesRuralDevelopment', 'Agriculture,Natural Resources,Rural Development'),
        ('audits', 'Audits'),
        ('education', 'Education'),
        ('energy', 'Energy'),
        ('engineering', 'Engineering'),
        ('finance', 'Finance'),
        ('health', 'Health'),
        ('industry&trade', 'Industry & Trade'),
        ('information&communicationtechnology', 'Information & Communication Technology'),
        ('marketing', 'Marketing'),
        ('multisector', 'Multisector'),
        ('publicsectormanagement', 'Public Sector Management'),
        ('operation&supplychain', 'Operation and Supply Chain'),
        ('socialenvironmentalandfinancialimpactassesments', 'social, environmental and financial impact assesments'),
        ('sustainabilityengineering', 'Sustainability Engineering'),
        ('transport', 'Transport'),
        ('waterandotherinfrastructureservices', 'Water and other Infrastructure Services'),
    ]
    name = models.CharField(max_length=255,choices=SECTOR_CHOICES)

    def __str__(self):
        return self.name


class Subsector(models.Model):
    name = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
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
    # sector_expertise = models.CharField(max_length=100,choices=SECTOR_CHOICES)
    # subsector_expertise = models.CharField(max_length=100, blank=True)
    # past_projects = models.TextField(blank=True)
    
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
    past_projects = models.ManyToManyField(PastProject, blank=True)
    sector_expertise = models.ManyToManyField(Sector)
    subsector_expertise = models.ManyToManyField(Subsector, blank=True)

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


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subject}"











