from django.views.generic import ListView , CreateView , DeleteView ,UpdateView , DetailView , FormView 
from .models import Project , Category , Task
from .forms import ProjectCreateForm , ProjectUpdateForm
from django.shortcuts import render , redirect
from django.urls import reverse_lazy , reverse

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')




class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project/update.html'
    
    def get_success_url(self) :
        return reverse('Project_Update' , args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'    
    success_url = reverse_lazy('Project_list')




class TaskCreateView(CreateView):
    model = Task
    fields = ['project' , 'description' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['us_completed' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    


class TaskDeleteView(DeleteView):
    model = Task
    
    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    

