from django.urls import path
from app1.views import *
app_name='vijay'
urlpatterns=[
    path('varisu/',varisu,name='varisu'),
]