from django import forms
from task_manager.statuses.models import TaskStatus


class StatuseForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ("name",)
