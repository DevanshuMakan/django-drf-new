from django.urls import path, include
from rest_framework import routers

from drf.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Courses', CourseViewSet)
router.register(r'Student', StudentViewSet)
router.register(r'Teacher', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]