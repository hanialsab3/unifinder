from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import University, Student, Application, Program

class SignUpForm(UserCreationForm):                           #add init function in case the boostrap is messed up
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

        # def __init__(self,*args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     self.fields['username'].label = "Display Name"
        #     self.fields['email'].label = "Email Address"

class EditProfileForm(UserChangeForm):                           #add init function in case the boostrap is messed up
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # username = forms.CharField(max_length=100)
    last_login = forms.CharField(max_length=100)
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput())
    date_joined = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ('user','profile_picture','name','website','phone','location','about')

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'use', 'type':'hidden'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'website': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'about': forms.Textarea(attrs={'class':'form-control'}),
        }

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('user','application_debug',)

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'use', 'type':'hidden'}),
            'application_debug': forms.TextInput(attrs={'class':'form-control'}),
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

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = ('uni','name','description')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }
