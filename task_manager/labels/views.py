from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.mixins import CustomLoginRequiredMixin, NoPermissionHandleMixin


class LabelsListView(NoPermissionHandleMixin, CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/list.html"
    context_object_name = "labels"
    ordering = ["date_joined"]


class LabelCreateView(SuccessMessageMixin, NoPermissionHandleMixin, CustomLoginRequiredMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelForm
    success_url = reverse_lazy("labels_list")
    success_message = _("Labels successfully created")


class LabelUpdateView(SuccessMessageMixin, NoPermissionHandleMixin, CustomLoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels_list")
    success_message = _("Label successfully changed")


class LabelDeleteView(SuccessMessageMixin, NoPermissionHandleMixin, CustomLoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels_list")
    success_message = _("Label deleted successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(self.request, _(
                "Cannot delete label because it is in use"))
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
