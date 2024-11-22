from django.urls import path
from Authentication import views

urlpatterns = [
    path('sign-in/',views.sign_in,name='sign-in'),
]