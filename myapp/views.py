from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def success(request):
    return render(request, 'success.html')

def landing(request):
    return render(request, 'landing.html')

def login1(request):
    return render(request,'login.html') 

def signup(request):
    return render(request,'signup.html') 

def signup_view(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logindetails')  # Replace 'success_url' with your actual URL name or path
        
        else:
            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    else: 
        form = Signup()
    
    return render(request, 'signup.html', {'form': form})
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Fixed typo from 'Password' to 'password'
        
        if not username or not password:
            return HttpResponse('Username and password are required')

        user1 = authenticate(request, username=username, password=password)
        if user1 is not None:
            login(request, user1)
            if user1.is_superuser:
                return redirect('admin')
            else:
                return redirect('registration')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')
    
@login_required
def user_registration1(request):
    form=None
    try:
        user_registration = UserRegistration.objects.get(user=request.user)
        form = UserRegistrationForm(instance=user_registration)  # Populate form with existing data
        already_registered = True
    except UserRegistration.DoesNotExist:
        user_registration = None
        already_registered = False
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user_registration = form.save(commit=False)
                user_registration.user = request.user
                user_registration.save()
                return redirect(reverse('profile')) 
            else:
                print(form.errors)  
    context = {
        'form': form,
        'already_registered': already_registered,
    }
    
    return render(request, 'profile.html', context)




def project_list(request):
    projects = Project_store.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})

def project_detail(request, project_id):
    projects = Project_store.objects.get(id=project_id)
    return render(request, 'project_details.html', {'projects': projects})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')  # Redirect to project list view after adding
    else:
        form = ProjectForm()
    return render(request, 'addproject.html', {'form': form})




@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

@login_required
def profile(request):
    user_registration = UserRegistration.objects.get(user=request.user)
    return render(request, 'profile.html', {'user_registration': user_registration})


# @login_required
# def profile(request):
#     # try:
#     user_registration = UserRegistration.objects.get(user=request.user)
#     # except UserRegistration.DoesNotExist:
#     #     user_registration = None
    
#     return render(request, 'profile.html', {'user_registration': user_registration})

@login_required
def apply_for_project(request, project_id):
    project = get_object_or_404(Project_store, id=project_id)
    user_registration = get_object_or_404(UserRegistration, user=request.user)
    
    if request.method == 'POST':
        form = ProjectApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user_details = user_registration
            application.project = project
            application.save()
            return redirect('project-list')
    else:
        form = ProjectApplicationForm()
    
    return render(request, 'apply.html', {'form': form, 'project': project})

@login_required
def my_applications(request):
    user_registration = get_object_or_404(UserRegistration, user=request.user)
    applications = ProjectApplication.objects.filter(user_details=user_registration)
    application_data = []
    for application in applications:
        project_store = application.project  # Access the Project_store object
        user_registration = application.user_details  # Access the UserRegistration object
        
        # Append relevant data to a list
        application_data.append({
            'project_title': project_store.title,
            'country':project_store.country,
            'open_to':project_store.open_to,
            'duration':project_store.duration,
            'sponsor':project_store.sponsor,
            'superviser':project_store.supervisor,
            'budget':project_store.budget,
            'deadline':project_store.deadline,
            'user_username': user_registration.user.username,
            'applied_on': application.applied_on,
            'remarks': application.remarks,
        })
    
    return render(request, 'my_applications.html', {'application_data': application_data})


