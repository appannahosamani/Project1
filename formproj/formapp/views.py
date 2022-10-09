from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request,'index.html')

def student_form_view(request):
    form=forms.student_form()
    return render(request,'form.html',{'form':form})