from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    mydict={'insert_me': 'iam Iron Man'}
    return render(request,'index.html',context=mydict)
def second(request):
    mydict2={'add_me':'iam Spider Man'}
    return render(request,'second.html',context=mydict2)