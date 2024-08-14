from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class UserUpdatePermissionMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return self.request.user == user
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _('You do not have the rights to change another user.'), extra_tags='danger')
            return redirect('users')
        messages.error(self.request, _('You are not logged in! Please log in.'), extra_tags='danger')
        return redirect('login')
        
    