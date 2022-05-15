from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from accounts.models import University, Student, Application
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from accounts.forms import ApplicationForm


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

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
        return context


def ApplyView(request):
    submitted = False
    if request.method == "POST":
        form = ApplicationForm(request.POST)
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
