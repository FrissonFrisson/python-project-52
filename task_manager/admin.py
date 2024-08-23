from django.contrib import admin
from task_manager.models import *

admin.site.register(Task)
admin.site.register(TaskStatus) 
admin.site.register(Label)
admin.site.register(LabelInfo)