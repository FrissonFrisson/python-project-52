from django.contrib import admin
from task_manager.tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'executor', 'status', 'date_joined')
    list_filter = ('status', 'date_joined')
    search_fields = ('name', 'description')
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
