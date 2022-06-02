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

class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ('profile_picture','name','website','phone','location','about')

        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.Textarea(attrs={'class':'form-control'}),
        }

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ('uni','student','motivation',"cv")

        widgets = {
            'uni': forms.Select(attrs={'class':'form-select'}),
            'student': forms.Select(attrs={'class':'form-select'}),
            'motivation': forms.TextInput(attrs={'class':'form-control'}),
            'cv': forms.TextInput(attrs={'class':'form-control'}),
        }


class UniversityProfileForm(ModelForm):
    class Meta:
        model = University
        fields = ('profile_picture','website','name','phone','location','about')

        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.TextInput(attrs={'class':'form-control'}),
        }


        def __init__(self, *args, **kwargs):
            # self.fields['user'] = kwargs.pop('user', None)
            # print(user)
            print(user)
            if model.objects.filter(user=1).exists():
                raise ValidationError("This user name already created a University!!!")
            self.user = user
            super(UniversityProfileForm, self).__init__(*args, **kwargs)
