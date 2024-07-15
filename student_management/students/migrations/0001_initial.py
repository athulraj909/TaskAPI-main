# Generated by Django 5.0.6 on 2024-07-05 06:45

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
            name='tbl_college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College', models.CharField(blank=True, max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coluser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(blank=True, max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enquiry_no', models.IntegerField(auto_created=True)),
                ('Enquiry_date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Gender', models.CharField(blank=True, max_length=50)),
                ('Qualification', models.CharField(blank=True, max_length=100)),
                ('Address', models.CharField(blank=True, max_length=200)),
                ('Contact_no', models.IntegerField()),
                ('WhatsApp_no', models.IntegerField()),
                ('DOB', models.DateField(blank=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='puser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experience', models.CharField(blank=True, max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
