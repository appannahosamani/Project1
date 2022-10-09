from django.db import models

# Create your models here.
class Myphotos(models.Model):
    name=models.CharField(max_length=200)
    pic=models.ImageField(null=True,blank=True,upload_to="images/%y")
    
class Meta:
    managed=False
    db_table=Myphotos