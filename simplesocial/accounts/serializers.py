from rest_framework import serializers
from .models import University,Student

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id','name','website','phone','location','about',]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','uni','application',]
