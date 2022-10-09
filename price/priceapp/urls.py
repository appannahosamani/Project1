from django.urls import path
from priceapp import views

app_name="priceapp"

urlpatterns=[
    path('',views.index),
    path('display/',views.display,name='display'),
]