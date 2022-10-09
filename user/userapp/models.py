from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofileinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


    #additional fields
    profile_img=models.ImageField(blank=True)
    profile_url=models.URLField(blank=True)

