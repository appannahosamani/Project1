from audioop import reverse
from pyexpat import model
from time import process_time
from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

class company(models.Model):
    name=models.CharField(max_length=200)
    ceo=models.CharField(max_length=200)
    origin=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('adminapp:details',kwargs={'pk':self.pk}')

class Mobiles(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    company=models.ForeignKey(company,related_name='company',on_delete=models.CASCADE)

    def __str__(self):
        return self.name