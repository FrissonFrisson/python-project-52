from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db.models.deletion import ProtectedError

from task_manager.statuses.models import TaskStatus
from task_manager.statuses.forms import StatuseForm
from task_manager.mixins import NoPermissionHandleMixin,CustomLoginRequiredMixin


class StatusesListView(NoPermissionHandleMixin,CustomLoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = "statuses/list.html"
    context_object_name = "statuses"
    ordering = ["date_joined"]


class StatusCreateView(NoPermissionHandleMixin,CustomLoginRequiredMixin, CreateView):
    template_name = "statuses/create.html"
    form_class = StatuseForm
    success_url = reverse_lazy("statuses_list")

    def form_valid(self, form):
        messages.success(self.request, _("Status successfully created"))
        return super().form_valid(form)


class StatusUpdateView(NoPermissionHandleMixin,CustomLoginRequiredMixin, UpdateView):
    model = TaskStatus
    form_class = StatuseForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses_list")

    def get_success_url(self):
        messages.success(self.request, _("Status successfully changed"))
        return super().get_success_url()


class StatusDeleteView(NoPermissionHandleMixin,CustomLoginRequiredMixin, DeleteView):
    model = TaskStatus
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, _("Status deleted successfully"))
            return redirect(self.get_success_url())
        except ProtectedError:
            messages.error(self.request, _("Cannot delete status because it is in use"))
            return redirect(self.get_success_url())
