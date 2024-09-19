from django import forms
from .models import Project


attrs = {'class': 'form-control'}

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category' , 'titel' , 'description' ]
        
        widgets = {
            'category' : forms.Select(attrs=attrs),
            'titel' : forms.TextInput(attrs=attrs),
            'description' : forms.Textarea(attrs=attrs),
        }


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category' , 'titel' , 'status' ]
        
        widgets = {
            'category' : forms.Select(attrs=attrs),
            'titel' : forms.TextInput(attrs=attrs),
            'status' : forms.Select(attrs=attrs),
        }