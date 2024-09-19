from django.urls import path , include
from django.contrib.auth.views import LoginView , LogoutView
from .forms import UserloginForm
from .views import logoutApp , RegisterView , edit_profile

urlpatterns = [

    path('login/' , LoginView.as_view(authentication_form = UserloginForm) , name = 'login'),
    path('register/' , RegisterView.as_view() , name = 'register'),
    path('logout',logoutApp , name='logout11'),
    path('profile',edit_profile , name='profile'),

    path('',include('django.contrib.auth.urls')),

]