from dataclasses import field
from django import forms
from priceapp.models import Products_Price

class Productform(forms.ModelForm):
    
    class Meta:
        model=Products_Price
        fields="__all__"