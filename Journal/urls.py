from django.urls import path
from Journal import views

urlpatterns = [
    path('journals/', views.journals, name='journals'),
    path('journal/<int:id>/', views.journal, name='journal')
]