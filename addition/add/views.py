from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def add(request):
    n1= int(request.POST['num1'])#n1= int(request.GET['num1']) GET is HTTP protocol method
    n2= int(request.POST['num2'])

    res=n1+n2
    
    
    return render(request,'result.html',{'Result':res})
def sub(request):
    n1= int(request.POST['num1'])
    n2=int(request.POST['num2'])
    r=n1-n2
    return render(request,'result.html',{'Result':r})