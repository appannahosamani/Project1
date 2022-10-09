from dataclasses import  fields

from django import forms
from user.models import User,userprofileinfo

class userprofileform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password')

class userprofileinfoform(forms.ModelForm):
    class Meta:
        model=userprofileinfo
        fields=('profile_img','profile_url')
