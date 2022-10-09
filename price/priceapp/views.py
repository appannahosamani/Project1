from django.shortcuts import render
from priceapp.forms import Productform
from priceapp.models import Products_Price

# Create your views here.
def index(request):
    
    if request.method=='POST':
        form = Productform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form =Productform()
    return render(request,'index.html',{"form":form})

def display(request):
    abc=Products_Price.objects.all()
    return render(request,'display.html',{'abc':abc})