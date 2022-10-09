from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def rolex(request):
    return render(request,'rolex.html')
def charlie(request):
    return render(request,'charlie.html')