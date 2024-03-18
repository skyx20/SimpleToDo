"""
URL configuration for Todo project.

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
from .models import Task
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/add/", views.add, name="add"),
    path("/edit/<int:task_id>", views.edit, name="edit"),
    path("/remove/<int:task_id>", views.remove, name="remove"),
    path("/delete/<int:task_id>", views.delete, name="delete"),
    path("admin/", admin.site.urls),
]
