from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'



    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance

class StudentCourseSerializer(serializers.ModelSerializer):
    Student_course = serializers.HyperlinkedIdentityField(view_name='course-detail')

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    Teacher_course = serializers.HyperlinkedIdentityField(view_name='course-detail', many=True)

    class Meta:
        model = Teacher
        fields = '__all__'

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            students = Student.objects.filter(courses=instance.student_course)
            representation['students'] = students.values()
            return representation



