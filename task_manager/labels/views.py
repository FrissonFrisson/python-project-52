from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from task_manager.mixins import CustomLoginRequiredMixin


class LabelsListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/list.html"
    context_object_name = "labels"
    ordering = ["date_joined"]


class LabelCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = "labels/create.html"
    form_class = LabelForm
    success_url = reverse_lazy("labels_list")

    def form_valid(self, form):
        messages.success(self.request, _("Labels successfully created"))
        return super().form_valid(form)


class LabelUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels_list")

    def get_success_url(self):
        messages.success(self.request, _("Label successfully changed"))
        return super().get_success_url()


class LabelDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, _("Label deleted successfully"))
            return redirect(self.get_success_url())
        except ProtectedError:
            messages.error(self.request, _("Cannot delete label because it is in use"))
            return redirect(self.get_success_url())
