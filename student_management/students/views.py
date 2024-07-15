from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import UserSerializer,PersonalSerializer,CollegeSerializer,CoursesSerializer,WorkSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.http import JsonResponse
import json
import jwt
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PersonelViewSet(viewsets.ModelViewSet):
    queryset = tbl_personal.objects.all()
    serializer_class = PersonalSerializer

class CollegeViewSet(viewsets.ModelViewSet):
    queryset = tbl_college.objects.all()
    serializer_class = CollegeSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = tbl_courses.objects.all()
    serializer_class = CoursesSerializer

class WorkviewSet(viewsets.ModelViewSet):
    queryset = tbl_work_experience.objects.all()
    serializer_class = WorkSerializer


def studentlog(data):
    user = User(username=data['username'],password=make_password(data['password']))
    user.save()
    return user


class StudentRegister(APIView):
    def post(self,request,format=None):
        try:
            student = request.data.get('student')
            print(student)
            data = request.data.get('data')
            print(data)
            stdlog = studentlog(student)
            print(stdlog)
            student_data = tbl_personal.objects.create(
                user_id = stdlog,
                Name = data['name'],
                Gender = data['gender'],
                Qualification = data['qualification'],
                Address = data['address'],
                Contact_no = data['contact'],
                WhatsApp_no = data['whatsapp'],
                DOB = data['dob']
            )
            student_data.save()
            print(f"Student : {student_data}")

            college_data = tbl_college.objects.create(user_id = stdlog,College = data['college'])
            college_data.save()
            print(f"College : {college_data}")

            course_data = tbl_courses.objects.create(user_id = stdlog,courses = data['courses'])
            course_data.save()
            print(f"Course : {course_data}")

            Workexperience_data = tbl_work_experience.objects.create(user_id = stdlog,Experience = data['experience'])
            Workexperience_data.save()
            print(f"Experience : {Workexperience_data}")

            data1 = {"status" : 1}
            return JsonResponse(data1,safe=False)

        except Exception as e:
            print(e)
            data1 = {"status" : 0}
            return JsonResponse(data1,safe=False)
            



class tokenLease(APIView):
    def post(self, request, format=None):                
        try:             
            userLogin = authenticate(request,username=request.data['username'],password=request.data['password'])            
            if userLogin is not None:
                vuser = User.objects.get(username=request.data['username'])
                auth_login(request, userLogin)                
                data = {"token":[], "status": []}
                each_item = {}
                each_item["token"] = jwt.encode({"phone":vuser.username},"secret",algorithm="HS256")                
                data["token"].append(each_item)
                each_item = {}
                each_item["status"] = 1
                data["status"].append(each_item)
                
                return JsonResponse(data,safe=False)
            else:
                data = []
                each_item = {}
                each_item["status"] = 0
                data.append(each_item)   

        except Exception as e:            
            print(e)
            data = []
            each_item = {}
            each_item["status"] = 0
            data.append(each_item)
            return JsonResponse(data,safe=False)




class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "username": user.username,
            "personal_info": {},
            "college_info": {},
            "course_info": {},
            "work_experience": {}
        }
        try:
            personal_info = tbl_personal.objects.get(user_id=user)
            user_data["personal_info"] = {
                "Name": personal_info.Name,
                "Gender": personal_info.Gender,
                "Qualification": personal_info.Qualification,
                "Address": personal_info.Address,
                "Contact_no": personal_info.Contact_no,
                "WhatsApp_no": personal_info.WhatsApp_no,
                "DOB": personal_info.DOB
            }
        except tbl_personal.DoesNotExist:
            pass

        try:
            college_info = tbl_college.objects.get(user_id=user)
            user_data["college_info"] = {
                "College": college_info.College
            }
        except tbl_college.DoesNotExist:
            pass

        try:
            course_info = tbl_courses.objects.get(user_id=user)
            user_data["course_info"] = {
                "courses": course_info.courses
            }
        except tbl_courses.DoesNotExist:
            pass

        try:
            work_experience = tbl_work_experience.objects.get(user_id=user)
            user_data["work_experience"] = {
                "Experience": work_experience.Experience
            }
        except tbl_work_experience.DoesNotExist:
            pass

        return JsonResponse(user_data)




class AllStudentsDetails(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        students_data = []

        personal_infos = tbl_personal.objects.all()
        for personal_info in personal_infos:
            user_data = {
                "username": personal_info.user_id.username,
                "personal_info": {
                    "Name": personal_info.Name,
                    "Gender": personal_info.Gender,
                    "Qualification": personal_info.Qualification,
                    "Address": personal_info.Address,
                    "Contact_no": personal_info.Contact_no,
                    "WhatsApp_no": personal_info.WhatsApp_no,
                    "DOB": personal_info.DOB
                },
                "college_info": {},
                "course_info": {},
                "work_experience": {}
            }

            try:
                college_info = tbl_college.objects.get(user_id=personal_info.user_id)
                user_data["college_info"] = {
                    "College": college_info.College
                }
            except tbl_college.DoesNotExist:
                pass

            try:
                course_info = tbl_courses.objects.get(user_id=personal_info.user_id)
                user_data["course_info"] = {
                    "courses": course_info.courses
                }
            except tbl_courses.DoesNotExist:
                pass

            try:
                work_experience = tbl_work_experience.objects.get(user_id=personal_info.user_id)
                user_data["work_experience"] = {
                    "Experience": work_experience.Experience
                }
            except tbl_work_experience.DoesNotExist:
                pass
            
            students_data.append(user_data)
        print(students_data)
            

        return JsonResponse(students_data,safe=False)



class SearchUsers(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
       
        name = request.data.get('name', None)
        qualification = request.data.get('qualification', None)
        contact_no = request.data.get('contact_no', None)
        college = request.data.get('college', None)

        query = Q()
        if name:
            query &= Q(Name__icontains=name)
        if qualification:
            query &= Q(Qualification__icontains=qualification)
        if contact_no:
            query &= Q(Contact_no__icontains=contact_no)
        if college:
            query &= Q(user_id__coluser__College__icontains=college)

        users = tbl_personal.objects.filter(query).distinct()

        results = []
        for user in users:
            user_data = {
                "Name": user.Name,
                "Gender": user.Gender,
                "Qualification": user.Qualification,
                "Address": user.Address,
                "Contact_no": user.Contact_no,
                "WhatsApp_no": user.WhatsApp_no,
                "DOB": user.DOB,
                "College": user.user_id.coluser.first().College if user.user_id.coluser.exists() else None
            }
            results.append(user_data)

        return JsonResponse({"status": 1, "results": results}, safe=False)




