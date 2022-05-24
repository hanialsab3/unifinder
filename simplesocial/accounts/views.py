# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS
from .serializers import UniversitySerializer, StudentSerializer, UserSerializer, ApplicationSerializer
from .models import University, Student, Application
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.decorators import login_required


from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly)    #IsAuthenticatedOrReadOnly



class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class ApplicationUserWritePermission(BasePermission):
    message = "Editing application is restricted to the student only."


    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.student.user == request.user


class ApplicationViewSet(viewsets.ModelViewSet, ApplicationUserWritePermission):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()            #.filter(uni=..)
    authentication_classes = (TokenAuthentication,)
    permission_classes = [ApplicationUserWritePermission]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [ApplicationUserWritePermission]
        else:
            permission_classes = [ApplicationUserWritePermission]
        return [permission() for permission in permission_classes]
