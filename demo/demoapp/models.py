
from django.db import models
from templates.student import h


# std=tabla_creditos()

# Create your models here.
# h = tabla_creditos()

class Creditos1(models.Model):

    sale_id = models.IntegerField(default=0)
    name = models.CharField(max_length=150)
    address=models.CharField(max_length=100)
    debe = models.IntegerField(default=0)

