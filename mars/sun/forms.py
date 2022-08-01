from dataclasses import fields
from django import forms
from sun.models import stockmodel

class stockform(forms.ModelForm):
    class Meta:
        model=stockmodel
        fields='__all__'