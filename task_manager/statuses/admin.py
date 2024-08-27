from django.contrib import admin
from task_manager.statuses.models import TaskStatus


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_joined')
    search_fields = ('name',)
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
