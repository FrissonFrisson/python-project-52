from django.urls import path
from .views import *

urlpatterns = [
    path('',TasksListView.as_view(), name = 'tasks_list'),
    path('create/', TaskCreateView.as_view(), name = 'create_task'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name = 'update_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view() , name = 'delete_task'),
    path('<int:pk>/', TaskDetail.as_view() , name = 'task_detail'),
]
