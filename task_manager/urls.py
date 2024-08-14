"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name = 'index' ),
    path('users/',UserListView.as_view(), name = 'users'),
    path('users/create/', RegistrationUser.as_view(), name = 'registration'),
    path('login/', CustomLoginUser.as_view(), name = 'login'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name = 'update_user'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view() , name = 'delete_user'),
    path('users/logout/', CustomLogoutUser.as_view(), name = 'logout'),
]
