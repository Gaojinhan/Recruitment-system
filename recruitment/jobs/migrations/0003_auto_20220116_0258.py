# Generated by Django 3.2.5 on 2022-01-16 02:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_auto_20220115_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': ('Job',), 'verbose_name_plural': 'Jobs'},
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=135)),
                ('city', models.CharField(max_length=135)),
                ('phone', models.CharField(max_length=135)),
                ('email', models.EmailField(blank=True, max_length=135)),
                ('apply_position', models.CharField(blank=True, max_length=135)),
                ('born_address', models.CharField(blank=True, max_length=135)),
                ('gender', models.CharField(blank=True, max_length=135)),
                ('bachelor_school', models.CharField(blank=True, max_length=135)),
                ('master_school', models.CharField(blank=True, max_length=135)),
                ('doctor_school', models.CharField(blank=True, max_length=135)),
                ('major', models.CharField(blank=True, max_length=135)),
                ('degree', models.CharField(blank=True, choices=[('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Phd', 'Phd')], max_length=135)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建日期')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('candidate_introduction', models.TextField(blank=True, max_length=1024)),
                ('work_experience', models.TextField(blank=True, max_length=1024)),
                ('project_experience', models.TextField(blank=True, max_length=1024)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
