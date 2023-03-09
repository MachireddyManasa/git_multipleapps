from django.urls import path
from app4.views import *
app_name='nothing'
urlpatterns=[
    path('manasa/',manasa,name='manasa'),
    path('siri/',siri,name='siri'),
]
