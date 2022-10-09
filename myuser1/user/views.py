from django.shortcuts import render
from user.forms import userprofileform,userprofileinfoform
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    registered=False
    if request.method == "POST":
        userform=userprofileform(data=request.POST)
        userprofileInfoform=userprofileinfoform(data=request.POST)
        if userform.is_valid() and userprofileInfoform.is_valid():
            user=userform.save()
            user.set_password(user.password)
            user.save()

            profile=userprofileInfoform.save(commit=False)
            profile.user=user

            profile.save()
            registered=True
        else:
            print(userform.errors,userprofileInfoform.errors)
    else:
        userform=userprofileform()
        userprofileInfoform=userprofileinfoform()

    return render(request,'registration.html',{'userform':userform,'userprofileInfoform':userprofileInfoform,'registered':registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
       

    
