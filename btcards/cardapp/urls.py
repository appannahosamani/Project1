from django.urls import path
from cardapp import views

app_name="cardapp"

urlpatterns=[
    path('rolex/',views.rolex,name='rolex'),
    path('charlie/',views.charlie,name='charlie')
]