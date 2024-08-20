from django.db.models.base import Model as Model
from django.http.request import HttpRequest as HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import *
from ..mixins import UserUpdatePermissionMixin
from django.contrib import messages
from django.views.generic import ListView



class UserListView(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    ordering = ['date_joined']
   

class RegistrationUser(CreateView):
    template_name = 'users/signup.html'
    form_class = SignUpForms
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, _('The user has been successfully registered'))
        return super().form_valid(form)
    

class CustomLoginUser(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        messages.success(self.request, _('You are logged in'))
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('index')


class CustomLogoutUser(LogoutView):
    next_page = reverse_lazy('index')

    def get_next_page(self) -> str | None:
        messages.info(self.request, _('You are logged out'))
        return super().get_next_page()



class UserUpdateView(UserUpdatePermissionMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')


    def get_success_url(self):
        messages.success(self.request, _('User successfully changed'))
        return super().get_success_url()

class UserDeleteView(UserUpdatePermissionMixin, DeleteView):
    model = User
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy("users")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _('User deleted successfully'))
        return super().delete(request, *args, **kwargs)