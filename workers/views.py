from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.views import LoginView,LogoutView,FormView   
from django.views.generic import DetailView, CreateView,UpdateView,FormView,ListView

from .forms import RegistrationForm,WorkerLoginForm
from users.models import UserProfile
from items.models import Item,ItemRental

# Create your views here.

class RegistrationView(FormView):
    form_class = RegistrationForm   
    template_name='worker/worker.html'
    success_url='/workers/login2/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




class ProfileDetailView(DetailView):
    model = UserProfile
    template_name="worker/profile.html"
    context_object_name = "profile" 
    is_me = False

    def get_object(self, queryset=None):
        if self.is_me:
            return self.request.user
        else:
            return super().get_object(queryset)
    def get_context_data(self, **kwargs):
        if self.is_me:
            context = super().get_context_data(**kwargs)
            o = UserProfile.objects.get(pk=self.request.user.id)
            context["itemrentals"] = ItemRental.objects.filter(hirer=o.id)
            context["is_me"] = self.is_me   
            return context
        else:
            context = super().get_context_data(**kwargs)
            o = UserProfile.objects.get(pk=self.kwargs['pk'])
            context["is_me"] = self.is_me   
            return context







class Login(LoginView):
    authentication_form = WorkerLoginForm
    form_class = WorkerLoginForm
    template_name = 'worker/login.html'
    success_url="/workers/profile/me/"
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']



        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)   



class JobsView(ListView):
    model = Item
    template_name = 'worker/jobs.html'  
    context_object_name = 'jobs'
    