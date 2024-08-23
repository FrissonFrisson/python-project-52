from django.urls import path
from task_manager.views import LabelsListView, LabelCreateView
from task_manager.views import LabelUpdateView, LabelDeleteView

urlpatterns = [
    path('', LabelsListView.as_view(), name='labels_list'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update_label'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete_label'),
]
