from django import forms
from django.contrib.auth.forms import AuthenticationForm



attrs = {'class': 'form-control'}



class UserloginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) :
        super(UserloginForm , self).__init__( *args, **kwargs)


    # Username2 = forms.CharField( label='Username' , widget=forms.TextInput(attrs=attrs))
    # Password = forms.CharField(label='Password' , widget=forms.PasswordInput(attrs=attrs))
