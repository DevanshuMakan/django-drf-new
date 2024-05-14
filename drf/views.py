from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import *

from .models import *

from drf.serializer import *


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentCourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,SessionAuthentication]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer