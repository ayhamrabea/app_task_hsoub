from django.shortcuts import render , redirect
from django.contrib.auth import logout

# Create your views here.

def logoutApp(request):
    logout(request)
    return redirect('login')