from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))

    def __str__(self):
        return self.name


class LabelInfo(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, verbose_name=_("Task"))
    label = models.ForeignKey(Label, on_delete=models.PROTECT, verbose_name=_("Label"))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    descriptions = models.TextField(verbose_name=_("Description"))
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name=_("Status"))
    label = models.ManyToManyField(Label, through="LabelInfo", verbose_name=_("Labels"))
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks_created', verbose_name=_("Author"))
    performer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='tasks_performed', verbose_name=_("Performer"))

    def __str__(self):
        return self.name
