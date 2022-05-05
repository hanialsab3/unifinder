# from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# class User(auth.models.User, auth.models.PermissionsMixin):
#
#     def __str__(self):
#         return "@{}".format(self.username)

class University(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    website = models.CharField(max_length=120)
    name = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, null=True)
    location = models.CharField(max_length=120, null=True)
    about = models.TextField(max_length=256, null=True)

    def __str__(self):
        if self.name==None:
            return "ERROR-UNIVERSITY NAME IS NULL"
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    application = models.CharField(max_length=120)
    uni = models.ManyToManyField(University, null=True)
    def __str__(self):
        return "Student: " + self.user.get_full_name()
