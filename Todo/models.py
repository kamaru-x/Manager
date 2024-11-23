from django.db import models

# Create your models here.

PRIORITY = (
    ('High', 'High'),
    ('Normal', 'Normal'),
    ('Low', 'Low'),
)

class Todo(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=250)
    priority = models.CharField(max_length=25, choices=PRIORITY)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title