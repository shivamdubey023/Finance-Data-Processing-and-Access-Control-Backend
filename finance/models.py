from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('viewer', 'Viewer')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class FinancialRecod(models.Model):
    TYPES_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]

    amount = models.FloatField()
    type = models.CharField(max_length=10, choices=TYPES_CHOICES)
    Category = models.ForeignKey(Category, on_delete= models.CASCADE)

    created_by = models.ForeignKey(User, related_name= 'created_records', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name= 'owned_records', on_delete= models.CASCADE)

    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.amount}"