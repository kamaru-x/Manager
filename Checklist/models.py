from django.db import models

# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Task(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date} / {self.title}'