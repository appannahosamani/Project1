from django.urls import path
from empapp import views

urlpatterns=[
    path('',views.index),
    path('empform',views.empform),
]