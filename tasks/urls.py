from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task_details/<int:id>', views.task_detail, name='detail'),
    path('change_status/<int:id>', views.change_status, name='change_status'),
    path('create_task', views.create_task, name='create_task'),
    path('my_tasks', views.user_tasks, name='user_tasks'),
    path('search', views.search, name='search'),
]
