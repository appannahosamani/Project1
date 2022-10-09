from dataclasses import field, fields
from pyexpat import model
from django import forms
from userapp.models import User,userprofileinfo

class userprofileform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')
class userprofileinfoform(forms.ModelForm):
    class Meta:
        model=userprofileinfo
        fields=('profile_img','profile_url')