from django.db import models

# Create your models here.

class Journal(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title