from django.db import models

# Create your models here.

TYPE = (
    ('Income', 'Income'),
    ('Expense', 'Expense')
)

class Category(models.Model):
    date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=25,choices=TYPE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Account(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    bank = models.CharField(max_length=50)
    number = models.CharField(max_length=25,default='XXXXXXXXXXXX')

    def __str__(self):
        return self.title

class Transaction(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=TYPE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    amount = models.FloatField(default=0.00)

    def __str__(self):
        return self.title