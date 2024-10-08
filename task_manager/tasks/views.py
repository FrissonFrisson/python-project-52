from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.tasks.models import Task
from task_manager.statuses.models import TaskStatus
from task_manager.labels.models import Label
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.filters import TaskFilter
from task_manager.mixins import NoPermissionHandleMixin, CustomLoginRequiredMixin


class TaskDetail(
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    DetailView
):
    model = Task
    template_name = "tasks/task.html"
    context_object_name = "task"


class TasksListView(
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    ListView
):
    model = Task
    template_name = "tasks/list.html"
    ordering = ["date_joined"]

    def get_queryset(self):
        tasks = Task.objects.all()
        tasks_filtered = TaskFilter(
            self.request.GET, queryset=tasks, request=self.request
        )
        return tasks_filtered

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["statuses"] = TaskStatus.objects.all()
        context["executor"] = User.objects.all()
        context["labels"] = Label.objects.all()
        context["filter"] = self.get_queryset()
        return context


class TaskCreateView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    CreateView
):
    template_name = "tasks/create.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks_list")
    success_message = _("Tasks successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task successfully changed")


class TaskDeleteView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    DeleteView
):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks_list")
    success_message = _("Task deleted successfully")

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        if self.object.author != request.user:
            messages.error(self.request, _(
                "Only its author can delete a task"))
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
