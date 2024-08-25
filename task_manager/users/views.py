from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from task_manager.mixins import UserUpdatePermissionMixin
from task_manager.users.forms import SignUpForms, LoginForm, CustomUserChangeForm


class UserListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"
    ordering = ["date_joined"]


class RegistrationUser(CreateView):
    template_name = "users/signup.html"
    form_class = SignUpForms
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, _("Пользователь успешно зарегистрирован"))
        return super().form_valid(form)


class CustomLoginUser(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, _("Вы вошли в систему"))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("index")


class CustomLogoutUser(LogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request):
        messages.info(self.request, _("Вы вышли из системы"))
        return super().dispatch(request)


class UserUpdateView(UserUpdatePermissionMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users")

    def get_success_url(self):
        messages.success(self.request, _("Пользователь успешно изменен"))
        return super().get_success_url()


class UserDeleteView(UserUpdatePermissionMixin, DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, _("Пользователь успешно удален"))
            return redirect(self.get_success_url())
        except ProtectedError:
            messages.error(
                self.request,
                _("Невозможно удалить пользователя, так как он используется"),
            )
            return redirect(self.get_success_url())
