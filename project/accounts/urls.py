from django.urls import path , include
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserloginForm
from .views import logoutApp

urlpatterns = [

    path('login/' , LoginView.as_view(authentication_form = UserloginForm) , name = 'login'),
    path('logout',logoutApp , name='logout11'),
    path('',include('django.contrib.auth.urls')),

]