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
        fields = [
            'user_type', 'name', 'firm_expertise', 'sector_expertise', 
            'subsector_expertise', 'past_projects', 'gender', 'state', 
            'city', 'pincode', 'course', 'email'
        ]
        widgets = {
            'sector_expertise': forms.TextInput(attrs={'placeholder': 'Add new sector'}),
            'subsector_expertise': forms.TextInput(attrs={'placeholder': 'Add new subsector'}),
            'past_projects': forms.Textarea(attrs={'placeholder': 'Add new past projects'}),
        }
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




class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['subject', 'message']

