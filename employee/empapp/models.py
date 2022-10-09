from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    address=models.CharField(max_length=200)