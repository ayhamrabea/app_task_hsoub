from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['category' , 'titel' , 'descriptin' ]
        
        widgets = {
            'category' : forms.Select(),
            'titel' : forms.TextInput(),
            'descriptin' : forms.Textarea(),
        }