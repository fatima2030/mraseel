from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView,UpdateView,FormView,ListView
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import UserRegisterForm,UserLoginForm,ProfileUpdateForm,UserWorkerForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetForm,PasswordChangeView
from django.contrib.auth import login
from django.views.generic.detail import BaseDetailView,DetailView,SingleObjectMixin
from django.conf import settings
from .models import UserProfile,working
from items.models import Item
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.db.models import Q
from items.models import ItemRental
from django.utils.translation import gettext, gettext_lazy as _



class RegistrationView(FormView):
    form_class = UserRegisterForm   
    template_name='user/register.html'
    success_url='/user/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Login(LoginView):
    authentication_form = UserLoginForm
    form_class = UserLoginForm
    template_name = 'user/login.html'
    success_url=''
    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']



        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)   


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = "user/password_reset.html"
    success_url='/'


class ProfileDetailView(DetailView):
    model = UserProfile
    template_name="user/profile.html"
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
        
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = ProfileUpdateForm
    template_name="user/profile_edit.html"
    success_url="/user/profile/me"
    def get_object(self, queryset=None):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'user/password_change.html'
    title = _('Password change')

class check(ListView):
    model = UserProfile
    template_name = 'home.html'
    context_object_name = 'check'

