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
    return render(request, 'index.html')

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
                return redirect('project-list')
            else:
                return redirect('registration')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')
    
# @login_required
# def user_registration1(request):
#     form=None
#     try:
#         user_registration = UserRegistration.objects.get(user=request.user)
#         form = UserRegistrationForm(instance=user_registration)  # Populate form with existing data
#         already_registered = True
#     except UserRegistration.DoesNotExist:
#         user_registration = None
#         already_registered = False
#         if request.method == 'POST':
#             form = UserRegistrationForm(request.POST)
#             if form.is_valid():
#                 user_registration = form.save(commit=False)
#                 user_registration.user = request.user
#                 user_registration.save()
#                 return redirect('profile') 
#             # else:
#             #     print(form.errors)  
#     context = {
#         'form': form,
#         'already_registered': already_registered,
#     }
    
#     return render(request, 'profile.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserRegistration
from .forms import UserRegistrationForm

# @login_required
# def user_registration1(request):
#     form = None
#     already_registered = False
    
#     try:
#         user_registration = UserRegistration.objects.get(user=request.user)
#         form = UserRegistrationForm(instance=user_registration)  # Populate form with existing data
#         already_registered = True
#     except UserRegistration.DoesNotExist:
#         user_registration = None
    
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, instance=user_registration)
#         if form.is_valid():
#             user_registration = form.save(commit=False)
#             user_registration.user = request.user

#             # Append new data to existing fields
#             if user_registration.sector_expertise:
#                 new_sectors = form.cleaned_data.get('sector_expertise')
#                 if new_sectors:
#                     user_registration.sector_expertise += '\,' + new_sectors

#             if user_registration.subsector_expertise:
#                 new_subsectors = form.cleaned_data.get('subsector_expertise')
#                 if new_subsectors:
#                     user_registration.subsector_expertise += '\,' + new_subsectors

#             if user_registration.past_projects:
#                 new_past_projects = form.cleaned_data.get('past_projects')
#                 if new_past_projects:
#                     user_registration.past_projects += '\n' + new_past_projects

#             user_registration.save()
#             return redirect('profile')
#         # else:
#         #     print(form.errors)
    
#     context = {
#         'form': form,
#         'already_registered': already_registered,
#     }
    
#     return render(request, 'profile.html', context)


# import datetime
# import uuid

# def generate_unique_id(user_type):
#     current_year = datetime.datetime.now().year
#     unique_id = uuid.uuid4().hex[:8].upper()  # Generate a unique 8-character hex string
#     return f'{current_year}-{user_type.upper()}-{unique_id}'





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
    # project_store=None
    for application in applications:
        project_store = application.project  # Access the Project_store object
        user_registration = application.user_details  # Access the UserRegistration object
        
        # Append relevant data to a list
        application_data.append({
            'id':project_store.id,
            'title': project_store.title,
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
    context={'application_data': application_data}
    return render(request, 'my_applications.html', context)


from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('landing')  



# EXCEL TO DATABASE

import pandas as pd
from datetime import datetime
from .models import Project_store

def import_projects_from_excel(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')  # Read Excel file
    
    for index, row in df.iterrows():
        # Extract data from each row
        title = row['title']
        supervisor = row['supervisor']
        tags = row['tags']
        country = row['country']
        open_to = row['open_to']
        duration = row['duration']
        sponsor = row['sponsor']
        deadline = row['deadline'].to_pydatetime().date()
        budget = row['budget']
        serial_no = row['serial_no']
        department = row['department']
        description = row['description']
        vacancy = row['vacancy']
        release_date = row['release_date'].to_pydatetime().date()
        eligibility = row['eligibility']
        expertise = row['expertise']

        # Create Project_store instance and save to database
        project = Project_store(
            title=title,
            supervisor=supervisor,
            tags=tags,
            country=country,
            open_to=open_to,
            duration=duration,
            sponsor=sponsor,
            deadline=deadline,
            budget=budget,
            serial_no=serial_no,
            department=department,
            description=description,
            vacancy=vacancy,
            release_date=release_date,
            eligibility=eligibility,
            expertise=expertise
        )
        project.save()


from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
 # Assuming import function is in the same directory

@login_required
@staff_member_required  # Ensures user is staff (admin)
def save_projects(request):
    if request.method == 'POST':
        try:
            file_path = "C:\\Users\\28pra\\OneDrive\\Desktop\\Call_for_Proposals.xlsx"  # Adjust path as necessary
            import_projects_from_excel(file_path)
            return redirect("project-list")
        except Exception as e:
            return HttpResponse(f'Error importing projects: {str(e)}')
    else:
        return HttpResponse('Invalid request method.')


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Project_store, UserProfile

@login_required
def bookmark_project(request, project_id):
    project = get_object_or_404(Project_store, id=project_id)
    user_profile = request.user.userprofile

    if project in user_profile.bookmarked_projects.all():
        user_profile.bookmarked_projects.remove(project)
        action = 'removed'
    else:
        user_profile.bookmarked_projects.add(project)
        action = 'added'

    # return JsonResponse({'action': action})
    return redirect('view_bookmarks')
@login_required
def view_bookmarks(request):
    user_profile = request.user.userprofile
    bookmarked_projects = user_profile.bookmarked_projects.all()
    return render(request, 'bookmarks.html', {'bookmarked_projects': bookmarked_projects})



def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('thankyou')  # Redirect to a thank-you page or any other page
    else:
        form = FeedbackForm()
    
    context = {
        'form': form,
    }
    return render(request, 'feedback.html', context)

def feedback_thank_you(request):
    return render(request, 'thankyou.html')

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def bookmark_project(request, project_id):
    project = get_object_or_404(Project_store, id=project_id)
    user_profile = request.user.userprofile

    if project in user_profile.bookmarked_projects.all():
        user_profile.bookmarked_projects.remove(project)
        action = 'removed'
    else:
        user_profile.bookmarked_projects.add(project)
        action = 'added'

    return redirect('project-list')

@login_required
def view_bookmarks(request):
    user_profile = request.user.userprofile
    bookmarked_projects = user_profile.bookmarked_projects.all()
    return render(request, 'bookmarks.html', {'bookmarked_projects': bookmarked_projects})

#### NEW ADDITION

# def registration_view(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.user = request.user
#             user.save()
#             return redirect('profile')  # Redirect to profile page or wherever after successful registration
#     else:
#         user_form = UserRegistrationForm()
    
#     context = {
#         'user_form': user_form,
#     }
#     return render(request, 'profile.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserRegistration, Sector, Subsector, PastProject
from .forms import UserRegistrationForm, SectorForm, SubsectorForm, PastProjectForm

@login_required
def registration_view(request):
    try:
        registration = UserRegistration.objects.get(user=request.user)
        already_registered = True
    except UserRegistration.DoesNotExist:
        registration = None
        already_registered = False

    if request.method == 'POST':
        if already_registered:
            form = UserRegistrationForm(request.POST, instance=registration)
        else:
            form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user_registration = form.save(commit=False)
            user_registration.user = request.user
            user_registration.save()
            form.save_m2m()
            return redirect('profile')
    else:
        if already_registered:
            form = UserRegistrationForm(instance=registration)
        else:
            form = UserRegistrationForm()

    context = {
        'form': form,
        'already_registered': already_registered,
        'registration': registration,
    }
    return render(request, 'profile.html', context)

@login_required
def add_sector(request):
    if request.method == 'POST':
        form = SectorForm(request.POST)
        if form.is_valid():
            sector = form.save()
            request.user.userregistration.sector_expertise.add(sector)
            return redirect('profile')
    else:
        form = SectorForm()

    context = {'form': form}
    return render(request, 'add_sector.html', context)

@login_required
def add_subsector(request):
    if request.method == 'POST':
        form = SubsectorForm(request.POST)
        if form.is_valid():
            subsector = form.save()
            request.user.userregistration.subsector_expertise.add(subsector)
            return redirect('profile')
    else:
        form = SubsectorForm()

    context = {'form': form}
    return render(request, 'add_sub_sector.html', context)

# from django.shortcuts import render, redirect
# from .forms import SubsectorForm

# def add_subsector(request):
#     print("add_subsector view called")  # Debug statement
#     if request.method == 'POST':
#         print("POST request received")  # Debug statement
#         form = SubsectorForm(request.POST)
#         if form.is_valid():
#             print("Form is valid")  # Debug statement
#             form.save()
#             return redirect('add_subsector')
#         else:
#             print("Form is not valid")  # Debug statement
#     else:
#         form = SubsectorForm()
    
#     return render(request, 'add_sub_sector.html', {'form': form})


@login_required
def add_past_project(request):
    if request.method == 'POST':
        form = PastProjectForm(request.POST)
        if form.is_valid():
            print("form is valid")
            past_project = form.save()
            request.user.userregistration.past_projects.add(past_project)
            return redirect('profile')
    else:
        form = PastProjectForm()
        print("form is not valid")

    context = {'form': form}
    return render(request, 'add_past_project.html', context)

