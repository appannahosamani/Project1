from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    age=models.PositiveIntegerField()
    email=models.EmailField()
