from django.contrib import admin
from django.urls import path, include
from task_manager.users.views import CustomLoginUser
from task_manager.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="index"),
    path("login/", CustomLoginUser.as_view(), name="login"),
    path("users/", include("task_manager.users.urls")),
    path("statuses/", include("task_manager.statuses.urls")),
    path("labels/", include("task_manager.labels.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
]
