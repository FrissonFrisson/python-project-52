from django import forms
from task_manager.models import Task_status
from django.utils.translation import gettext_lazy as _


class StatuseForm(forms.ModelForm):
    class Meta:
        model = Task_status
        fields = ('name',)
