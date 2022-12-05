from django.urls import path 
from . import views

urlpatterns = [
    path('',views.apiOverView, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-details/<int:pk>', views.task_details, name='task-details'),
    path('task-create/', views.task_create, name='task-create'),
    path('task-update/<int:pk>', views.task_update, name='task-update'),
    path('task-delete/<int:pk>', views.task_delete, name='task-delete')
]