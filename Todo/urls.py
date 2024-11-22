from django.urls import path
from Todo import views

urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/add/', views.add_todo, name='add-todo'),
    path('todo/complete/<int:id>/', views.mark_todo_completed, name='mark-todo-completed'),
]