from django.urls import path
from taskapp import views

app_name="taskapp"

urlpatterns=[
    path('mytask/',views.mytask,name='mytask'),
]