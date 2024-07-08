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
    user_type = forms.ChoiceField(choices=UserRegistration.USER_TYPE_CHOICES)
    dord_number = forms.CharField(required=False)
    name = forms.CharField(required=True)
    firm_expertise = forms.CharField(widget=forms.Textarea, required=False)
    sector_expertise = forms.CharField(required=True)
    subsector_expertise = forms.CharField(required=False)
    past_projects = forms.CharField(widget=forms.Textarea, required=False)
    gender = forms.ChoiceField(choices=UserRegistration.GENDER_CHOICES)
    state = forms.CharField(required=True)
    city = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    course = forms.CharField(required=False)
    
    class Meta:
        model = UserRegistration
        fields = ['user_type','dord_number', 'name', 'firm_expertise', 'sector_expertise', 'subsector_expertise', 'past_projects', 'gender', 'state', 'city', 'pincode', 'course']

    def save(self, commit=True):
        user_registration = super().save(commit=False)
        if commit:
            user_registration.save()
        return user_registration



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_store
        fields = '__all__'


class ProjectApplicationForm(forms.ModelForm):
    class Meta:
        model = ProjectApplication
        fields = ['remarks']