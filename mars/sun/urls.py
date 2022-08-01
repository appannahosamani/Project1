from django.urls import path
from . import views

app_name='sun'

urlpatterns=[
    path('index/',views.index,name='index'),
    path('inventory/',views.inventory,name='inventory'),
    path('schedule/',views.schedule,name='schedule'),
    path('delete/',views.delete,name='delete')
]