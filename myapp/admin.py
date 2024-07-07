from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserRegistration)

@admin.register(Project_store)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'country', 'deadline', 'budget')
    list_filter = ('country', 'deadline')
    search_fields = ('title', 'supervisor', 'tags', 'sponsor')
    date_hierarchy = 'deadline'




