from rest_framework import serializers
from .models import University,Student
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id','user','name','website','phone','location','about','no_of_students']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','uni','application',]
