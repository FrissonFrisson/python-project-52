from django.urls import path
from task_manager.users import views
from .views import *

urlpatterns = [
    path('',LabelsListView.as_view(), name = 'labels_list'),
    path('create/', LabelCreateView.as_view(), name = 'create_label'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name = 'update_label'),
    path('<int:pk>/delete/', LabelDeleteView.as_view() , name = 'delete_label'),
]
