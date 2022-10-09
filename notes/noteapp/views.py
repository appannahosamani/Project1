from django.shortcuts import render
from templates import students
# Create your views here.
def index(request):
    return render(request,'index.html',context=students.my_dict)

def java(request):
    return render(request,'javastd.html',students.my_dict)

def javap(request):
    return render(request,'javapri.html',students.my_dict)

def python(request):
    return render(request,'pythonstd.html',context=students.my_dict)

def pythp(request):
    return render(request,'pythpri.html',context=students.my_dict)

def java1(request):
    return render(request,'java1.html',context=students.my_dict)

def home(request):
    return render(request,'index.html',context=students.my_dict)