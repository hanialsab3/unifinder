from django.views.generic import TemplateView, CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from accounts.models import University, Student, Application, Program
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.forms import ApplicationForm, UniversityProfileForm, UniversityForm, StudentForm, ProgramForm
from django.core.exceptions import ValidationError


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['students'] = Student.objects.all()[:5]
        context['universities'] = University.objects.all()[:5]
        return context

class DebugView(TemplateView):
    template_name = 'debug.html'

class UniversityListView(ListView):
    model = University
    paginate_by = 100  # if pagination is desired
    template_name = 'university_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['programs'] = Program.objects.all()
        return context

class AddUniversityView(CreateView):
    model = University
    form_class = UniversityForm
    template_name = 'add_university.html'

class StudentProfileView(DetailView):
    model = Student
    template_name = 'student_profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AddStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    # fields =

class UpdateUniversityView(UpdateView):
    model = University
    template_name = 'update_university.html'
    form_class = UniversityForm
    # fields = ('profile_picture','name','website','phone','location','about')


def ApplyView(request):
    submitted = False
    if request.method == "POST":
        form = ApplicationForm(request.POST,initial={'user': request.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/apply?submitted=True')
    else:
        form = ApplicationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'apply.html', {'form':form, 'submitted':submitted})


class ApplicationListView(ListView):
    model = Application
    paginate_by = 100  # if pagination is desired
    # queryset = Application.objects.filter(student=self.request.user)
    template_name = 'application_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ApplicationDetailView(DetailView):

    model = Application
    template_name = 'application_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# class ProfilePage(DetailView):
#     model = University
#     paginate_by = 100  # if pagination is desired
#     template_name = 'profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

def ProfilePageView(request):
    model = University
    submitted = False
    exists = False
    if request.method == "POST":
        form = UniversityProfileForm(request.POST,request.FILES)
        if form.is_valid():
            if model.objects.filter(user=request.user).exists():
            # raise ValidationError("This user name already created a University")
                return HttpResponseRedirect('/profile?exists=True')
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/profile?submitted=True')
    else:
        form = UniversityProfileForm
        if 'submitted' in request.GET:
            submitted = True
        if 'exists' in request.GET:
            exists = True
    return render(request, 'profile.html', {'form':form, 'submitted':submitted, 'exists':exists})


class ProgramDetailView(DetailView):

    model = Program
    template_name = 'program_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AddProgramView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'add_program.html'

class UpdateProgramView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'add_program.html'
    # fields =
