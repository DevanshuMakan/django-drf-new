from django.db import models

# Create your models here.
class Course(models.Model):
    Course_name = models.CharField(max_length=255)
    Course_code = models.CharField(max_length=255)
    Course_duration = models.IntegerField()
    Course_fee = models.IntegerField()

    def __str__(self):
        return self.Course_name


class Student(models.Model):
    Student_name = models.CharField(max_length=255)
    Student_email = models.CharField(max_length=255)
    Student_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.Student_name

class Teacher(models.Model):
    Teacher_name = models.CharField(max_length=255)
    Teacher_course = models.ManyToManyField(Course)

    def __str__(self):
        return self.Teacher_name