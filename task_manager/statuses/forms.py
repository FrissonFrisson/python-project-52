from django import forms
from task_manager.models import TaskStatus
from django.utils.translation import gettext_lazy as _


class StatuseForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ('name',)
