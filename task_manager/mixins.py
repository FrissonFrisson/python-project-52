from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class UserPermissionDeniedMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _(
                "You do not have the rights to change another user.")
        self.permission_denied_url = reverse_lazy('users')
        return super().dispatch(request, *args, **kwargs)


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = _('You are not logged in! Please sign in.')
        self.permission_denied_url = reverse_lazy('login')
        return super().dispatch(request, *args, **kwargs)


class NoPermissionHandleMixin():

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)