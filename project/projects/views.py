from django.views.generic import ListView , CreateView , DeleteView ,UpdateView , DetailView , FormView 
from .models import Project , Category , Task
from .forms import ProjectCreateForm , ProjectUpdateForm
from django.shortcuts import render , redirect
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin



# (4) LoginRequiredMixin     لكي نتأكد من تسجيل الدخول لكي لا يعرض المعلومات
# (5)  UserPassesTestMixin     لكي نتأكد من أن المشروع معروض من قبل صاحبه فقط
 


class ProjectListView(LoginRequiredMixin , ListView):  #  (4) LoginRequiredMixin   نقوم بتوريثها في كل الدوال
    model = Project
    template_name = 'project/list.html'
    paginate_by = 6

    def  get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id' : self.request.user}   # قمنا بكتابة شرط لكي يظهر مشاريع المستخدم فقط
        q = self.request.GET.get('q',None)
        if q:where['titel'] = q
        return query_set.filter(**where)
    


class ProjectCreateView(LoginRequiredMixin , CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_list')

    def form_valid(self, form):   #   قمنا بكتابة دالة لكي يأخد المشروع id ال user
        form.instance.user = self.request.user
        return super().form_valid(form)
    




class ProjectUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project/update.html'

    def test_func(self):    # (5) لكي نتحقق من صاحب المشروع و المستخدم الحالي
        return self.get_object().user_id == self.request.user.id   #  when this function returns false the page doesn't work

    
    def get_success_url(self) :
        return reverse('Project_Update' , args=[self.object.id])




class ProjectDeleteView(LoginRequiredMixin , DeleteView):
    model = Project
    template_name = 'project/delete.html'    
    success_url = reverse_lazy('Project_list')




class TaskCreateView(LoginRequiredMixin , CreateView):
    model = Task
    fields = ['project' , 'description' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    


class TaskUpdateView(LoginRequiredMixin , UpdateView):
    model = Task
    fields = ['us_completed' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    


class TaskDeleteView(LoginRequiredMixin , DeleteView):
    model = Task
    
    def get_success_url(self):
        return reverse('Project_Update' , args=[self.object.project.id])
    

