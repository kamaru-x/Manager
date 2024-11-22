from django.urls import path
from Timesheet import views

urlpatterns = [
    path('timesheet/',views.timesheet,name='timesheet')
]