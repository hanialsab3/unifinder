from django.views.generic import TemplateView
from rest_framework import viewsets
from accounts.serializers import UniversitySerializer
from accounts.models import University
from rest_framework.authentication import TokenAuthentication

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()
    authentication_classes = (TokenAuthentication,)
