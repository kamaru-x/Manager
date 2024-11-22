from django.urls import path
from Transactions import views

urlpatterns = [
    path('category/add/',views.add_category,name='add-category'),
    path('category/delete/<int:id>/',views.delete_category,name='delete-category'),

    path('account/add/',views.add_account,name='add-account'),
    path('account/delete/<int:id>/',views.delete_account,name='delete-account'),

    path('transaction/',views.transactions,name='transactions'),
    path('transaction/add/',views.add_transaction,name='add-transaction'),
    path('transaction/delete/<int:id>/',views.delete_transaction,name='delete-transaction'),

    path('fetch-categories/', views.fetch_categories, name='fetch-categories'),
]