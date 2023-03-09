from app3.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('mother/',mother,name='mother'),
    path('father/',father,name='father'),
]