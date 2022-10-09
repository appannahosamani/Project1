#creating separate urls for application
from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.index),
    path('second/',views.second)
]