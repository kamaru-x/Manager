from django.contrib import admin
from Todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'priority', 'is_completed']

admin.site.register(Todo,TodoAdmin)