from django.db import models
from django.utils.translation import gettext_lazy as _


class TaskStatus(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name=_("Name"))

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))

    def __str__(self):
        return self.name
