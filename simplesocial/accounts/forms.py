from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import University, Student, Application

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('university','motivation',"cv")

        widgets = {
            'university': forms.Select(attrs={'class':'form-select'}),
            'motivation': forms.TextInput(attrs={'class':'form-control'}),
            'cv': forms.TextInput(attrs={'class':'form-control'}),
        }
