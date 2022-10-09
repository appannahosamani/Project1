from django import forms

class student_form(forms.Form):
    Name=forms.CharField(max_length=200)
    Phone=forms.IntegerField()
    age=forms.IntegerField()
    text=forms.CharField(widget=forms.Textarea)
   