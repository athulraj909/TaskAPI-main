from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter
from students.views import UserViewSet, PersonelViewSet, CollegeViewSet,CourseViewSet,WorkviewSet

router = DefaultRouter()
router.register('user', UserViewSet)
router.register('personal', PersonelViewSet)
router.register('college', CollegeViewSet)
router.register('course', CourseViewSet)
router.register('work', WorkviewSet)





urlpatterns = [
    path('register/student',StudentRegister.as_view(),name="studentregister"),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('token/', tokenLease.as_view()),
    path('profile/', UserProfile.as_view(), name='profile'),
    path('students/', AllStudentsDetails.as_view(), name='all_students_details'),
    path('search/users', SearchUsers.as_view(), name='search_users'),
    

]