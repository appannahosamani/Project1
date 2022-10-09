from django.urls import path
from urlapp import views

app_name='urlapp'


urlpatterns=[
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
    path('contact/',views.contact,name='contact'),
]