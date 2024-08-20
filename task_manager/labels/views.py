from django.http.request import HttpRequest as HttpRequest
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from task_manager.models import Label
from .forms import *
from ..mixins import UserUpdatePermissionMixin
from django.contrib import messages
from django.views.generic import ListView



class LabelsListView(ListView):
    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'
    ordering = ['date_joined']
   

class LabelCreateView(CreateView):
    template_name = 'labels/create_labels.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels_list')

    def form_valid(self, form):
        messages.success(self.request, _('Labels successfully created'))
        return super().form_valid(form)
    

class LabelUpdateView(UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update_label.html'
    success_url = reverse_lazy('labels_list')


    def get_success_url(self):
        messages.success(self.request, _('Label successfully changed'))
        return super().get_success_url()

class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'labels/delete_label.html'
    success_url = reverse_lazy("labels_list")

    def get_success_url(self):
        messages.success(self.request, _('Label successfully deleted'))
        return super().get_success_url()