from django.views.generic import ListView , CreateView ,DeleteView , DetailView , FormView 
from .models import Project , Category , Task
from .forms import ProjectCreateForm
from django.shortcuts import render 
from django.urls import reverse_lazy

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')
    