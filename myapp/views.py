from django.shortcuts import render, redirect,HttpResponse
from .forms import *

def success(request):
    return render(request, 'success.html')

def landing(request):
    return render(request, 'landing.html')

def login(request):
    return render(request,'login.html') 

from django.contrib.auth import authenticate, login
from django.contrib import messages

def signup(request):
    return render(request,'signup.html') 

# def dashboard(request):
#     return render(request,'dashboard.html') 

def signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration.html')  # Replace 'success_url' with your actual URL name or path
        
        else:
            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    else: 
        form = Signup()
    
    return render(request, 'signup.html', {'form': form})

# def user_registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'registration.html', {'form': form})

# def user_registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('logindetails')  # Ensure 'login' is correctly configured in your urls.py
#         else:
#             print(form.errors)  # Print errors to help debug form validation issues
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'registration.html', {'form': form})


# def register_ceo(request):
#     if request.method == 'POST':
#         form = CEOSignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             CEO_group = Group.objects.get(name='CEO')
#             CEO_group.user_set.add(user)
#             login(request, user)
#             return redirect('custom_login')
#         else:
#             # Capture form errors and display them
#             return render(request, 'signupceo_form.html', {'form': form, 'role': 'CO', 'errors': form.errors})
#     else:
#         form = CEOSignUpForm()
#     return render(request, 'signupceo_form.html', {'form': form, 'role': 'CO'})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Fixed typo from 'Password' to 'password'
        
        if not username or not password:
            return HttpResponse('Username and password are required')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('dashboard')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')

from django.shortcuts import render, redirect


def project_list(request):
    projects = Project_store.objects.all(user=request.user)
    return render(request, 'dashboard.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')  # Redirect to project list view after adding
    else:
        form = ProjectForm()
    return render(request, 'addproject.html', {'form': form})


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def projectdetails(request):
    return render(request,'project_details.html')

# @login_required
# def profile(request):
#     user = request.user
#     return render(request, 'profile.html', {'user': user})
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import UserRegistration

def register(request):
    if request.method == 'POST':
        user_form = Signup(request.POST)
        registration_form = UserRegistrationForm(request.POST)
        if user_form.is_valid() and not(registration_form.is_valid()):
            user = user_form.save()
            
            user_registration.user = user
            user_registration.save()
            return render(request,'registration.html') 
        elif not (user_form.is_valid()) and registration_form.is_valid():
            # user = user_form.save()
            user_registration = registration_form.save(commit=False)
            user_registration.user = user
            user_registration.save()
            return redirect('profile')
        elif user_form.is_valid() and registration_form.is_valid():
            user = user_form.save()
            user_registration = registration_form.save(commit=False)
            user_registration.user = user
            user_registration.save()
            login(request, user)
            return redirect('logindetails')
        else:
            context = {'user_form': user_form,'registration_form': registration_form,'errors': form.errors}
            return render(request, 'signup.html', context)
    else:
        user_form = UserSignUpForm()
        registration_form = UserRegistrationForm()
    
    context = {
        'user_form': user_form,
        'registration_form': registration_form
    }
    
    return render(request, 'registration.html', context)

def profile(request):
    user_registration = UserRegistration.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'user_registration': user_registration})


@login_required
def profile(request):
    user_registration = UserRegistration.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_registration': user_registration})
