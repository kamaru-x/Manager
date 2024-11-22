from django.contrib import admin
from Journal.models import Journal

# Register your models here.

class JournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']

admin.site.register(Journal,JournalAdmin)