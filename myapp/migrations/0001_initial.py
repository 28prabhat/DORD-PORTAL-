# Generated by Django 5.0.6 on 2024-07-10 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('supervisor', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('open_to', models.CharField(max_length=200)),
                ('sponsor', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('serial_no', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('vacancy', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('eligibility', models.TextField()),
                ('expertise', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('admin', 'Admin (DORD)'), ('dean', 'Dean'), ('staff', 'Staff'), ('faculty', 'Faculty of IITK'), ('researchScholar', 'Research Scholars of IITK'), ('sectionB', 'Section B companies'), ('siicCompanies', 'SIIC Incubated companies'), ('projectStaff', 'Project Staff')], max_length=20)),
                ('dord_number', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('firm_expertise', models.TextField(blank=True)),
                ('sector_expertise', models.CharField(max_length=100)),
                ('subsector_expertise', models.CharField(blank=True, max_length=100)),
                ('past_projects', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project_store')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userregistration')),
            ],
        ),
    ]
