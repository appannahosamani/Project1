from django.urls import path
from adminapp import views

app_name="adminapp"

urlpatterns=[
    path('list/',views.companylist.as_view(),name='list'),
    # path('details/',views.companydetails.as_view(),name='details'),
    path("<int:pk>",views.companydetails.as_view(),name="detail"),
]