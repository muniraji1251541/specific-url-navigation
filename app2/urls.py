from django.urls import path
from app2.views import *
app_name='ajith'
urlpatterns=[
    path('thunivu/',thunivu,name='thunivu'),
]