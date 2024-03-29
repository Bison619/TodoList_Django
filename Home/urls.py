"""
URL configuration for TodoList project.

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

from django.urls import path
from . import views
from .views import update_task

urlpatterns = [

    path('',views.index,name='home'),
    path('task/',views.task, name='task'),
    path('delete/<int:task_id>', views.del_task),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('task/<int:task_id>/', views.Completedtask, name='Completedtask'),
    path('task/cdelete/<int:task_id>', views.del_ctask),
]
