from django.contrib import admin
from Transactions.models import Category, Account, Transaction

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['date', 'type', 'title']

admin.site.register(Category,CategoryAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'bank', 'number']

admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'type', 'category', 'amount']

admin.site.register(Transaction,TransactionAdmin)