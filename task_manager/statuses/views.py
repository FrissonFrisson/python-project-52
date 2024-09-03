from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.statuses.models import TaskStatus
from task_manager.statuses.forms import StatuseForm
from task_manager.mixins import NoPermissionHandleMixin, CustomLoginRequiredMixin


class StatusesListView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    ListView
):
    model = TaskStatus
    template_name = "statuses/list.html"
    context_object_name = "statuses"
    ordering = ["date_joined"]


class StatusCreateView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    CreateView
):
    template_name = "statuses/create.html"
    form_class = StatuseForm
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully created")


class StatusUpdateView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    UpdateView
):
    model = TaskStatus
    form_class = StatuseForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status successfully changed")


class StatusDeleteView(
    SuccessMessageMixin,
    NoPermissionHandleMixin,
    CustomLoginRequiredMixin,
    DeleteView
):
    model = TaskStatus
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses_list")
    success_message = _("Status deleted successfully")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.task_set.exists():
            messages.error(self.request, _(
                "Cannot delete status because it is in use"))
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
