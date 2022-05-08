from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from .views import UniversityViewSet, StudentViewSet


app_name = 'accounts'
router = routers.DefaultRouter()
router.register('Universitys', UniversityViewSet)
router.register('Students', StudentViewSet)


urlpatterns = [
    url(r'login/$',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$',views.SignUp.as_view(),name='signup'),
    path('api', include(router.urls)),
]
