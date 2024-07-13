# myapp/forms.py

from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm



class Signup(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email' ,'password1', 'password2']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['user_type', 'name', 'firm_expertise', 'gender', 'state', 'city', 'pincode', 'course', 'email']

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['name']

class SubsectorForm(forms.ModelForm):
    class Meta:
        model = Subsector
        fields = ['sector', 'name']

class PastProjectForm(forms.ModelForm):
    class Meta:
        model = PastProject
        fields = ['project_name', 'country', 'state', 'start_date', 'end_date', 'client',
                  'funding_obtained', 'grant_number', 'details']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_store
        fields = '__all__'


class ProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ['remarks']




class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']

