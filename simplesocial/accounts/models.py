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

    def __str__(self):
        return "University: " + self.user.get_full_name()

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    application = models.CharField(max_length=120)
    def __str__(self):
        return "Student: " + self.user.get_full_name()
