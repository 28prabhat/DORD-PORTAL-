"""
URL configuration for dordportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from myapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', landing, name='landing'),
    path('registration', registration_view, name='registration'),
    path('add_sector/', add_sector, name='add_sector'),
    path('add_subsector/', add_subsector, name='add_subsector'),
    path('add_past_project/', add_past_project, name='add_past_project'),
    path('success/', success, name='success'),
    path('login/', custom_login, name='login'),
    path('signup/', signup, name='signup'),
    path('signupview/', signup_view, name='signupview'),
    path('logindetails/', custom_login, name='logindetails'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/', project_list, name='project-list'),
    path('projects/add/', add_project, name='add-project'),
    path('project/<int:project_id>/', project_detail, name='projectdetail'),
    path('profile/', profile, name='profile'),
    path('projects/apply/<int:project_id>/', apply_for_project, name='applyforproject'),
    path('my_applications/', my_applications, name='myapplications'),
    path('logout/', logout_user, name='logout'),
    path('addproject/', save_projects, name='save_projects'),
    path('bookmark_project/<int:project_id>/', bookmark_project, name='bookmark_project'),
    path('bookmarks/', view_bookmarks, name='view_bookmarks'),
     path('feedback/', feedback, name='feedback'),
    path('feedback/thank-you/', feedback_thank_you, name='thankyou'),


    

]
