from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category' , 'titel' , 'description' ]
        
        widgets = {
            'category' : forms.Select(),
            'titel' : forms.TextInput(),
            'description' : forms.Textarea(),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category' , 'titel' , 'status' ]
        
        widgets = {
            'category' : forms.Select(),
            'titel' : forms.TextInput(),
            'status' : forms.Select(),
        }