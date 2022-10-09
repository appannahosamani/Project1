from django.db import models

# Create your models here.
class Products_price(models.Model):
    Product_Name=models.CharField(max_length=200)
    Product_Price=models.IntegerField()
    Product_Image= models.ImageField(upload_to="images/%y")
    Product_description=models.TextField()

    