from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class indexView(TemplateView):
    # def home(self,request):
    #     template_name='home.html'

    
    template_name = 'index.html'
