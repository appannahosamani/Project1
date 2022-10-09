from django.shortcuts import render
from sal.forms import employeeform

# Create your views here.
def home(request):
    f=employeeform()
    return render(request,'home.html',{'fm':f})

def cal(request):
    form=employeeform()
    return render(request,'calsal.html',{'form':form})
    # if request.method=="POST":
        
