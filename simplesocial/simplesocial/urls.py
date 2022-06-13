"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from . import views
from accounts.views import UniversityViewSet, StudentViewSet,UserViewSet, ApplicationViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('Universitys', UniversityViewSet)
router.register('Students', StudentViewSet)
router.register('Applications', ApplicationViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    path('api/', include(router.urls)),
    path('auth/',obtain_auth_token),
    url(r'^accounts/',include('accounts.urls',namespace='accounts')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    path('students/add/', views.AddStudentView.as_view(), name='add_student'),
    path('students/edit/<int:pk>/', views.UpdateStudentView.as_view(), name='student_profile'),
    path('students/<int:pk>/', views.StudentProfileView.as_view(), name='student_profile'),
    path('universities/', views.UniversityListView.as_view(), name='university-list'),
    path('universities/<int:pk>/', views.UniversityDetailView.as_view(), name='university-detail'),
    path('universities/add/', views.AddUniversityView.as_view(), name='add_university'),
    path('universities/edit/<int:pk>/', views.UpdateUniversityView.as_view(), name='update_university'),
    path('universities/<int:pk>/remove', views.DeleteUniversityView.as_view(), name='delete_university'),
    path('programs/<int:pk>/', views.ProgramDetailView.as_view(), name='program-detail'),
    path('programs/add/', views.AddProgramView.as_view(), name='add_program'),
    path('programs/edit/<int:pk>/', views.UpdateProgramView.as_view(), name='update_program'),
    path('debug/',views.DebugView.as_view(),name='debug'),
    path('apply/',views.ApplyView,name='apply'),
    path('applications', views.ApplicationListView.as_view(), name='application-list'),
    path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('profile/', views.ProfilePageView, name='profile'),
    path('docs/', include_docs_urls(title='UnifinderAPI')),
    path('schema', get_schema_view(
        title="Unifinder API",
        description="API for updating records",
        version="1.0.0"
    ), name='openapi-schema'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
