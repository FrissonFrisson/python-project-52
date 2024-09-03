from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.forms import (
    SignUpForms,
    LoginForm,
    CustomUserChangeForm
)
from django.shortcuts import redirect
from task_manager.mixins import NoPermissionHandleMixin, CustomLoginRequiredMixin, UserPermissionDeniedMixin
from django.contrib import messages
from django.views.generic import ListView
from django.db.models.deletion import ProtectedError


class UserListView(ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    ordering = ['date_joined']


class RegistrationUser(SuccessMessageMixin, CreateView):
    template_name = 'users/signup.html'
    form_class = SignUpForms
    success_url = reverse_lazy('login')
    success_message = _('The user has been successfully registered')


class CustomLoginUser(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
    success_message = _('You are logged in')


class CustomLogoutUser(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request):
        messages.info(self.request, _('You are logged out'))
        return super().dispatch(request)


class UserUpdateView(SuccessMessageMixin, CustomLoginRequiredMixin, NoPermissionHandleMixin, UserPermissionDeniedMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully changed')


class UserDeleteView(SuccessMessageMixin, NoPermissionHandleMixin, CustomLoginRequiredMixin, UserPermissionDeniedMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy("users")
    success_message = _('User deleted successfully')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.tasks_created.exists() or self.object.tasks_author.exists():
            messages.error(self.request, _(
                "Cannot delete user because it is in use"))
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
