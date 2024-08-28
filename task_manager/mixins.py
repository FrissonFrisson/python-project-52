from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class UserPermissionDeniedMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _(
                "You do not have the rights to change another user."))
            return redirect("users")
        return super().handle_no_permission()


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def __init__(self) -> None:
        self.permission_denied_message = _(
            "You are not logged in! Please log in.")
        self.redirect_url = "login"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.permission_denied_message)
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
