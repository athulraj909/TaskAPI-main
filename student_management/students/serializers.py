from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']



class PersonalSerializer(serializers.ModelSerializer):
    user = UserSerializer() #author connect AuthorSerializer
    class Meta:
        model = tbl_personal
        fields = ['user','Enquiry_no','Enquiry_date','Name','Gender','Qualification','Address','Contact_no','WhatsApp_no','DOB']


class CollegeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = tbl_college
        fields = ['user','College']


class CoursesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = tbl_courses
        fields = ['user','courses']

class WorkSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = tbl_work_experience
        fields = ['user','Experience']