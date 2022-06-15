from django.conf.urls import url,include
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUp


app_name = 'accounts'



urlpatterns = [
    # url(r'login/$',
    #     auth_views.LoginView.as_view(template_name='accounts/login.html'),
    #     name='login'),
    # url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',SignUp.as_view(),name='signup'),

]
