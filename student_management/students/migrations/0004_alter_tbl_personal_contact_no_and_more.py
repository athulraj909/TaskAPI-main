# Generated by Django 5.0.6 on 2024-07-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_tbl_personal_enquiry_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_personal',
            name='Contact_no',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='tbl_personal',
            name='Name',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tbl_personal',
            name='WhatsApp_no',
            field=models.IntegerField(unique=True),
        ),
    ]
