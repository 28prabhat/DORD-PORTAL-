# Generated by Django 5.0.6 on 2024-07-13 08:18

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
            name='PastProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.CharField(max_length=255)),
                ('funding_obtained', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('grant_number', models.CharField(max_length=100)),
                ('details', models.TextField()),
            ],
        ),
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
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('agricultureNaturalResourcesRuralDevelopment', 'Agriculture,Natural Resources,Rural Development'), ('audits', 'Audits'), ('education', 'Education'), ('energy', 'Energy'), ('engineering', 'Engineering'), ('finance', 'Finance'), ('health', 'Health'), ('industry&trade', 'Industry & Trade'), ('information&communicationtechnology', 'Information & Communication Technology'), ('marketing', 'Marketing'), ('multisector', 'Multisector'), ('publicsectormanagement', 'Public Sector Management'), ('operation&supplychain', 'Operation and Supply Chain'), ('socialenvironmentalandfinancialimpactassesments', 'social, environmental and financial impact assesments'), ('sustainabilityengineering', 'Sustainability Engineering'), ('transport', 'Transport'), ('waterandotherinfrastructureservices', 'Water and other Infrastructure Services')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.sector')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmarked_projects', models.ManyToManyField(blank=True, related_name='bookmarked_by', to='myapp.project_store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),
                ('course', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('past_projects', models.ManyToManyField(blank=True, to='myapp.pastproject')),
                ('sector_expertise', models.ManyToManyField(to='myapp.sector')),
                ('subsector_expertise', models.ManyToManyField(blank=True, to='myapp.subsector')),
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
