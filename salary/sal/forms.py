from dataclasses import fields
from pyexpat import model
from django import forms
from sal.models import employee

class employeeform(forms.ModelForm):
    class Meta:
        model= employee
        fields='__all__'