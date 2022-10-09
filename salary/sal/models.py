from django.db import models

# Create your models here.
class employee(models.Model):
    name= models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=200)
    Basic_sal=models.IntegerField()
    No_of_OT=models.IntegerField()
    