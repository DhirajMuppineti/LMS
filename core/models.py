from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    bio = models.CharField(null=True, max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(default="default.jpg", upload_to="profiles_pics")
    

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    def __str__(self):
        return self.student.name

class Teacher(models.Model):
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher.name

class Subject(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    name = models.CharField(max_length = 250) 
    description = models.TextField(null= True)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="course_images/", blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Chapter(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length = 250)
    content = CKEditor5Field()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.title
