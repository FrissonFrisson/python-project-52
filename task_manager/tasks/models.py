from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=_("Name"))

    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Joined"))

    description = models.TextField(verbose_name=_("Description"))

    status = models.ForeignKey(
        'statuses.TaskStatus', on_delete=models.PROTECT, verbose_name=_("Status")
    )

    labels = models.ManyToManyField(
        'labels.Label', verbose_name=_("Labels"), blank=True
    )

    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.PROTECT,
        related_name="tasks_created",
        verbose_name=_("Author"),
    )

    executor = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.PROTECT,
        related_name="tasks_executor",
        verbose_name=_("Executor"),
    )

    def __str__(self):
        return self.name
