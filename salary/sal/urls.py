from django.urls import path
from sal import views

urlpatterns=[
    path('',views.home),
    path('cal',views.cal),
]