from django.urls import path

from task_manager.users.views import (
    UserListView,
    RegistrationUser,
    UserUpdateView,
    UserDeleteView,
    CustomLogoutUser,
    CustomLoginUser
)

urlpatterns = [
    path("", UserListView.as_view(), name="users"),
    path("create/", RegistrationUser.as_view(), name="registration"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update_user"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete_user"),
    path("logout/", CustomLogoutUser.as_view(), name="logout")
]
