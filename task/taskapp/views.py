from crypt import methods
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def mytask(request):
    if request.method=='POST':
        
        t1=request.POST['task1']
        t2=request.POST['task2']
        t3=request.POST['task3']
        t4=request.POST['task4']
        return render(request,'taskpage.html',{'t1':t1,'t2':t2,'t3':t3,'t4':t4} )
