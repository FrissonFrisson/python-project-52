from django.http.request import HttpRequest as HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from task_manager.models import Task
from .forms import *
from ..mixins import UserUpdatePermissionMixin
from django.contrib import messages
from django.views.generic import ListView



class TasksListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    ordering = ['date_joined']
   

class TaskCreateView(CreateView):
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        messages.success(self.request, _('Tasks successfully created'))
        return super().form_valid(form)
    

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update_Task.html'
    success_url = reverse_lazy('tasks_list')


    def get_success_url(self):
        messages.success(self.request, _('Task successfully changed'))
        return super().get_success_url()

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/delete_Task.html'
    success_url = reverse_lazy("tasks_list")

    def get_success_url(self):
        messages.success(self.request, _('Task successfully deleted'))
        return super().get_success_url()