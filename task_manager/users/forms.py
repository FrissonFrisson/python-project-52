from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    BaseUserCreationForm,
)
from django.contrib.auth.models import User


class SignUpForms(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

    def __init__(self, *args, **kwargs):
        super(SignUpForms, self).__init__(*args, **kwargs)
        if "usable_password" in self.fields:
            del self.fields["usable_password"]


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class CustomUserChangeForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username")

    def __init__(self, *args, **kwargs):
        super(BaseUserCreationForm, self).__init__(*args, **kwargs)
        if "usable_password" in self.fields:
            del self.fields["usable_password"]
