from django import forms
from task_manager.models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name','descriptions', 'status', 'label', 'performer' )
