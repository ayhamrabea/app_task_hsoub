from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm , UserChangeForm
from django.contrib.auth.models import User

attrs = {'class': 'form-control'}



class UserloginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs) :
        super(UserloginForm , self).__init__( *args, **kwargs)


    # Username2 = forms.CharField( label='Username' , widget=forms.TextInput(attrs=attrs))
    # Password = forms.CharField(label='Password' , widget=forms.PasswordInput(attrs=attrs))



class CreateUserForm(UserCreationForm):

    first_name = forms.CharField( label='First Name' , widget=forms.TextInput(attrs=attrs))
    last_name = forms.CharField( label='Last Name' , widget=forms.TextInput(attrs=attrs))
    username = forms.CharField( label='Username' , widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField( label='Email' , widget=forms.TextInput(attrs=attrs))
    password1 = forms.CharField( label='Password' , strip = False , widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField( label='Password Confirmation' , strip = False , widget=forms.PasswordInput(attrs=attrs))

    class Meta(UserCreationForm.Meta):
        fields = ['first_name' , 'last_name' , 'username' , 'email' ]


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email' ]

        widgets = {
            'first_name' : forms.TextInput(attrs=attrs),
            'last_name' : forms.TextInput(attrs=attrs),
            'email' : forms.EmailInput(attrs=attrs),
        }
