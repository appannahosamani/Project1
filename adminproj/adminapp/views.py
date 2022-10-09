from django.shortcuts import render
from adminapp.models import company,Mobiles
from django.http import HttpResponse
from . import models
from django.views.generic import View,TemplateView,ListView,DetailView

# Create your views here.
# class CBVviews(View):
#     def get(self,request):
#         return HttpResponse("Bad guys to kill...!")

class indexView(TemplateView):
    template_name='index.html'

class companylist(ListView):
    model = company
    template_name = 'adminapp/company_list.html'

class companydetails(DetailView):
    context_object_name='objects'
    model=company
    template_name='adminapp/company_details.html'

    def __str__(self):
        return self.name
        