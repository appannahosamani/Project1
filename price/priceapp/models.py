
from django.db import models


# Create your models here.
class Products_Price(models.Model):
    Product_name=models.CharField(max_length=200)
    Product_Price=models.IntegerField()
    Product_Image=models.ImageField(upload_to="images/%y" )
    Product_Description=models.TextField()

    def __str__(self):
        return self.Product_name

class Meta:
    managed=False
    db_table=Products_Price  