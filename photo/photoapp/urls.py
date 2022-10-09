from django.urls import path
from photoapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('details',views.details,name='details'),
]