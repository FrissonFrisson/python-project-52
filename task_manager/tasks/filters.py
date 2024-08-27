import django_filters
from django.utils.translation import gettext_lazy as _
from django import forms

from task_manager.tasks.models import Task
from task_manager.statuses.models import TaskStatus
from task_manager.labels.models import Label
from task_manager.users.models import CustomUser


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=_("Status"),
        queryset=TaskStatus.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_("Executor"), queryset=CustomUser.objects.all()
    )
    labels = django_filters.ModelChoiceFilter(
        label=_("Label"), queryset=Label.objects.all()
    )
    author = django_filters.BooleanFilter(
        label=_("Only my tasks"),
        method="filter_author",
        widget=forms.CheckboxInput(),
    )

    class Meta:
        model = Task
        fields = ["status", "executor"]

    def filter_author(self, queryset, name, value):
        if value:
            return queryset.filter(**{"author__id": self.request.user.id})
        return queryset
