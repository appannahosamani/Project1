from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')
# def add(request):
#     n1=int(request.GET["num1"])
#     n2=int(request.GET["num2"])
#     res=n1+n2
#     return render(request,'result.html',{"result":res})
def calclulator(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    if request.POST['sub'] == '+':
        return render(request,'result.html',{"result":n1+n2})
    elif request.POST['sub'] == '-':
        return render(request,'result.html',{"result":n1-n2})
    elif request.POST['sub'] == '*':
        return render(request,'result.html',{"result":n1*n2})
    elif request.POST['sub'] == '/':
        return render(request,'result.html',{"result":n1//n2})
    elif request.POST["sub"] == '%':
        return render(request,'result.html',{"result":n1%n2})
def home(request):
    return render(request,'index.html')
    
    