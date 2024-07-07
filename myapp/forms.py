# myapp/forms.py

from django import forms
from .models import *
from django.contrib.auth.models import User


# class UserRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = UserRegistration
#         fields = '__all__'  # Or list all the fields explicitly

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserRegistration

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
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
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type', 'dord_number', 'name', 'firm_expertise', 'sector_expertise', 'subsector_expertise', 'past_projects', 'gender', 'state', 'city', 'pincode', 'course']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user_registration = UserRegistration.objects.create(
                user=user,
                user_type=self.cleaned_data['user_type'],
                dord_number=self.cleaned_data['dord_number'],
                name=self.cleaned_data['name'],
                firm_expertise=self.cleaned_data['firm_expertise'],
                sector_expertise=self.cleaned_data['sector_expertise'],
                subsector_expertise=self.cleaned_data['subsector_expertise'],
                past_projects=self.cleaned_data['past_projects'],
                gender=self.cleaned_data['gender'],
                state=self.cleaned_data['state'],
                city=self.cleaned_data['city'],
                pincode=self.cleaned_data['pincode'],
                course=self.cleaned_data['course'],
                email=self.cleaned_data['email']
            )
        return user


from django.contrib.auth.forms import UserCreationForm


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project_store
        fields = '__all__'


