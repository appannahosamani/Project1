from dataclasses import fields
from django import forms
from empapp.models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields="__all__"
