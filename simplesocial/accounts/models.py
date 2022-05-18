# from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)

class University(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True)
    website = models.CharField(max_length=120)
    name = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, null=True)
    location = models.CharField(max_length=120, null=True)
    about = models.TextField(max_length=256, null=True)

    def no_of_students(self):
        students = Student.objects.filter(uni=self)
        return len(students)

    def __str__(self):
        if self.name==None:
            return "ERROR-UNIVERSITY NAME IS NULL"
        return self.name

    def get_absolute_url(self):
        return reverse("university-detail", args=[str(self.id)])

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    application_debug = models.CharField(max_length=120)
    uni = models.ManyToManyField(University)
    def __str__(self):
        return "Student: " + self.user.get_full_name()


class Application(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    uni = models.ForeignKey(University, on_delete=models.CASCADE)
    motivation = models.CharField(max_length=120)  #file
    cv = models.CharField(max_length=120)

    def __str__(self):
        return "Application Number " + str(self.id)

    def get_absolute_url(self):
        return reverse("application-detail", args=[str(self.id)])
