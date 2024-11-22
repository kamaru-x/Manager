from django.contrib import admin
from Checklist.models import Title, Task

# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Title,TitleAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'is_completed']

admin.site.register(Task,TaskAdmin)