from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class SignUpForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def __init__(self, *args, **kwargs):
        super(SignUpForms, self).__init__(*args, **kwargs)


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CustomUserChangeForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

        