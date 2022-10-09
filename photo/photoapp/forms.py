from django import forms
from photoapp.models import Myphotos

class photoform(forms.ModelForm):
    class Meta:
        model=Myphotos
        fields="__all__"