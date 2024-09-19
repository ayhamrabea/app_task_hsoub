from django.shortcuts import render , redirect
from django.contrib.auth import logout , login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateUserForm , ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def logoutApp(request):
    logout(request)
    return redirect('login')


class RegisterView(CreateView):
    form_class = CreateUserForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_success_url(self) :
        login(self.request , self.object)
        return reverse_lazy('Project_list')
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        return render(request , 'profile.html' , {'form' : form})
