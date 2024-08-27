from django.contrib import admin
from task_manager.labels.models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_joined')
    search_fields = ('name',)
    date_hierarchy = 'date_joined'
    ordering = ('-date_joined',)
