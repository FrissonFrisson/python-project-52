from django.http.request import HttpRequest as HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.models import Task_status
from .forms import *
from ..mixins import UserUpdatePermissionMixin
from django.contrib import messages
from django.views.generic import ListView



class StatusesListView(ListView):
    model = Task_status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    ordering = ['date_joined']
   

class StatusCreateView(CreateView):
    template_name = 'statuses/create_status.html'
    form_class = StatuseForm
    success_url = reverse_lazy('statuses_list')

    def form_valid(self, form):
        messages.success(self.request, _('Status successfully created'))
        return super().form_valid(form)
    

class StatusUpdateView(UpdateView):
    model = Task_status
    form_class = StatuseForm
    template_name = 'statuses/update_status.html'
    success_url = reverse_lazy('statuses_list')


    def get_success_url(self):
        messages.success(self.request, _('Status successfully changed'))
        return super().get_success_url()

class StatusDeleteView(DeleteView):
    model = Task_status
    template_name = 'statuses/delete_status.html'
    success_url = reverse_lazy("statuses_list")

    def get_success_url(self):
        messages.success(self.request, _('Status deleted successfully'))
        return super().get_success_url()