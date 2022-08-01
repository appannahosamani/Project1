from ast import Not
from asyncio.windows_events import NULL
from django.shortcuts import render
from sun.forms import stockform
from .models import stockmodel
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import RangeOperators
from django.db.models import *
# from django.http import HttpResponse

# Create your views here...
def home(request):
    return render(request,'home.html')

def index(request):
    form=stockform()
    if request.method=='POST':
        form=stockform(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'index.html', {'result':form})

def inventory(request):
    invent=stockmodel.objects.all()
    return render(request,'inventory.html',{'invent':invent})

def schedule(request):
    aaa=stockmodel.objects.all()
    abs={
        'arun':[
            {'date':'10/03/2019','Packet_Id':'F1','Packet_Type':'Food','Packet_content':'MRE','Calories':1000,'Expiry_Date':'07/05/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'F4','Packet_Type':'Food','Packet_content':'Rice','Calories':1500,'Expiry_Date':'06/05/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'W2','Packet_Type':'Water','Packet_content':NULL,'Calories':NULL,'Expiry_Date':NULL,'Quantity_in_Litres':2},

            {'date':'11/03/2019','Packet_Id':'F2','Packet_Type':'Food','Packet_content':'Protien bar','Calories':2000,'Expiry_Date':'06/06/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'F9','Packet_Type':'Food','Packet_content':'Rice','Calories':500,'Expiry_Date':'05/07/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'W3','Packet_Type':'Water','Packet_content':NULL,'Calories':NULL,'Expiry_Date':NULL,'Quantity_in_Litres':2},

            {'date':'12/03/2019','Packet_Id':'F3','Packet_Type':'Food','Packet_content':'Dry fruits','Calories':1000,'Expiry_Date':'27/06/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'F6','Packet_Type':'Food','Packet_content':'Apple pie','Calories':1500,'Expiry_Date':'06/06/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'W5','Packet_Type':'Water','Packet_content':NULL,'Calories':NULL,'Expiry_Date':NULL,'Quantity_in_Litres':2},

            {'date':'13/03/2019','Packet_Id':'F5','Packet_Type':'Food','Packet_content':'Biscuits','Calories':1000,'Expiry_Date':'31/12/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'F7','Packet_Type':'Food','Packet_content':'MRE','Calories':1000,'Expiry_Date':'07/07/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'F8','Packet_Type':'Food','Packet_content':'Biscuits','Calories':500,'Expiry_Date':'05/07/2019','Quantity_in_Litres':NULL},
            {'Packet_Id':'W1','Packet_Type':'Water','Packet_content':NULL,'Calories':NULL,'Expiry_Date':NULL,'Quantity_in_Litres':1},
            {'Packet_Id':'W4','Packet_Type':'Water','Packet_content':NULL,'Calories':NULL,'Expiry_Date':NULL,'Quantity_in_Litres':1}
        
        ]
    }

    return render(request,'schedule.html',context=abs)

def delete(request):
    return render(request,'delete.html')
    
    
    # d1={'day1':'10/06/2022','day2':'11/06/2022','day3':'12/06/2022'}
    # for i in d1:
    #     if i=='day1':





     # abs=stockmodel.objects.all()
    # return render(request,'schedule.html',{'abs':abs})


    # if request.method=='POST':
    #     std=stockmodel.objects.all()

        



        # id=request.GET.get('id',None)
        # if id is not None:
        #     ss=[stockmodel.id,stockmodel.Packet_Id,stockmodel.Packet_Type,stockmodel.Packet_content,stockmodel.Calories,stockmodel.Expiry_Date,stockmodel.Quantity_in_Litres]
            
        #     return render(request,'schedule.html',{'ss':ss})

    # sh=stockmodel.objects.all()
    # field1={
    #     "f1":[
    #         {stockmodel.objects.all().distinct('Packet_Id'=='F1' and 'Calories'==1000)},
    #         {stockmodel.objects.all().distinct('Packet_Id'=='F4' and 'Calories'==1500)},
    #         {stockmodel.objects.all().distinct('Packet_Id'=='W1' and 'Quantity_in_Litres'==2)}

    #     ]
    # # }
    # db=stockmodel.objects.all()
    # for id in db:
    #     abc={}
    #     if id ==1:
    #         abc={
    #             "abc":[
    #                 {'id': stockmodel(id)==1 },
    #                 {'id5': stockmodel(id)==5},
    #                 {'id2': stockmodel(id)==2}
                   
    #         ] 
    #         }


    #         return HttpResponse(request,'schedule.html',{'abc':abc})


    # if (stockmodel.Packet_Id=="F1" and  stockmodel.Packet_Id=="F4" and stockmodel.Calories(id==)) 
    # for id in db:
    #     if id ==1:
    #         abc={
    #             "abc":[
    #                 {stockmodel.Packet_Id(),stockmodel.Packet_Type(),stockmodel.Packet_content(),stockmodel.Calories(),stockmodel.Expiry_Date(),stockmodel.Quantity_in_Litres(

    #                 ) },
                   
    #         ] 
    #         }


    #         return render(request,'schedule.html',{'abc':abc})



   

    # return render(request,'schedule.html',{'invent':invent})

     
        
        
    # fid=stockmodel.Packet_Id.get()
    # fcal=stockmodel.Calories.get()
    




# def select_date(request):
#     client = Client.objects.all()
#     process = Client_Process.objects.all()
#     pdf = Client_files.objects.all()
#     today = date.today()
#     yesterday = today - timedelta(days = 1)
#     print(today)
#     print(yesterday)
#     if request.method == "POST":
#         fromdate = request.POST.get('fromdate')
#         todate = request.POST.get('todate')
#         user = Client_files.objects.filter(Date__range=(fromdate,todate))
#         print(user)
#     return render(request,'select_date.html', {'pdf':pdf,'client':client,'process':process})





# Create your views here.

# def showformdata(request):
#     # if request.method == 'POST':
#     #     fm = stockform(request.POST)
#     #     if fm.is_valid():
#     #         nm = fm.cleaned_data['Packet_Id']
#     #         em = fm.cleaned_data['Packet_Type']
#     #         pw = fm.cleaned_data['Packet_content']
#     #         pa = fm.cleaned_data['Calories']
#     #         pb = fm.cleaned_data['Expiry_Date']
#     #         pc = fm.cleaned_data['Quantity_in_Litres']
#     #         reg = stockmodel(id==26)
#     #         reg.delete()
#     # else:
#     date=3
#     fm = stockmodel.objects.all()
#     return render(request,'schedule.html',{'form':fm,'date':date})