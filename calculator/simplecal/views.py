from django.shortcuts import render


# Create your views here.
def index(request):
   
    return render(request,'index.html')
def add(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    # res=n1+n2
    # return render(request,'result.html',{'Result':res})
    if request.POST["cal"]== '+' :
        return render(request,'index.html',{'Result':n1+n2})#i have replacing result.html to index.html
    elif request.POST['cal']=='-':
        return render(request,'index.html',{'Result':n1-n2})
    elif request.POST['cal']=='*':
        return render(request,'index.html',{'Result':n1*n2})
    elif request.POST['cal']=='/':
        return render(request,'index.html',{'Result':n1//n2})
    elif request.POST['cal']=='%':
        return render(request,'index.html',{'Result':n1%n2})

''' 
                or 

    if 'add' in request.POST:
        res=n1+n2
    elif 'sub' in request.POST:
        res=n1-n2
    elif 'mul' in request.POST:
        res=n1*n2
    elif 'div' in request.POST:
        res=n1//n2
    elif 'mod' in request.POST:
        res=n1%n2
    return render(request,'result.html',{'Result':res})    '''
