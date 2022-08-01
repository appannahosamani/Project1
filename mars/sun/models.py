from statistics import mode
from django.db import models

# Create your models here.
class stockmodel(models.Model):
    Packet_Id=models.CharField(max_length=200,blank=True,null=True)
    Packet_Type=models.CharField(max_length=200,blank=True,null=True)
    Packet_content=models.CharField(max_length=200,blank=True,null=True)
    Calories=models.IntegerField(blank=True,null=True)
    Expiry_Date=models.DateField(blank=True,null=True)
    Quantity_in_Litres=models.IntegerField(blank=True,null=True) 

class Meta:
    managed=False
    db_table=stockmodel
