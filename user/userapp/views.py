
from django.shortcuts import render
from xml.dom.domreg import registered
from userapp.forms import userprofileform,userprofileinfoform

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    registered=False
    if request.method=='POST':
        userform=userprofileform(data=request.POST)
        userprofileInfoform=userprofileinfoform(data=request.POST)

        if userform.is_valid() and userprofileInfoform.is_valid():
            user=userprofileInfoform.save()
            user.set_password(user.password)
            user.save()

            profile=userprofileInfoform.save(commit=False)
            profile.user=user #make connection between user module and our module
            
            profile.save()

            registered=True
        else:
            print(userform.errors,userprofileInfoform.errors)
    else:
        userform=userprofileform()
        userprofileInfoform=userprofileinfoform()


    return render(request,'registration.html',{'form1':userform,'form2':userprofileInfoform,'registered':registered})