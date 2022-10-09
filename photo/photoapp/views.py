from django.shortcuts import render
from photoapp.forms import photoform
from photoapp.models import Myphotos
# Create your views here.
def index(request):
    
    if request.method=="POST":
        form =photoform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,'index.html',{'obj':obj})
    else:
        form= photoform()
    img=Myphotos.objects.all()

    return render(request,'index.html',{'form':form})

def details(request):
    form = Myphotos.objects.all()
    return render(request,'details.html',{'form':form})

# def details(request):
#     form = photoform()
#     if request.method=="POST":
#         form =photoform(request.POST)
#         if form.is_valid():
#             form.save()

#         return render(request,'details.html',{'form':form})