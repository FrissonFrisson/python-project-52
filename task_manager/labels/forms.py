from django import forms
from task_manager.models import Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)
