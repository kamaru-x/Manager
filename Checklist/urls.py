from django.urls import path
from Checklist import views

urlpatterns = [
    path('checklist/', views.checklist, name='checklist'),
    path('checklist/complete/<int:id>/', views.mark_task_completed, name='mark-task-completed'),
    path('tasks/<str:date>/', views.tasks, name='tasks'),
]