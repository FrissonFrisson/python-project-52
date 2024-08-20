from django.urls import path
from task_manager.users import views
from .views import *

urlpatterns = [
    path('',StatusesListView.as_view(), name = 'statuses_list'),
    path('create/', StatusCreateView.as_view(), name = 'create_status'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name = 'update_status'),
    path('<int:pk>/delete/', StatusDeleteView.as_view() , name = 'delete_status'),
]
