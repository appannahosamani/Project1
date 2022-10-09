from django.shortcuts import render
from empapp.forms import employeeform

# Create your views here.
def index(request):
    return render(request,'index.html')

def empform(request):
    form=employeeform()

    if request.method=="POST":
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'form.html',{'form':form})