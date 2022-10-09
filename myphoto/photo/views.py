from operator import imod
from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.

def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # obj=form.instance
            # return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
    # img=Image.objects.all()
    return render(request,"index.html",{"form":form})

def display(request):
    pics=Image.objects.all()
    return render(request,'display.html',{'pics':pics})
