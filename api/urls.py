from . import views
from django.urls import path

urlspatterns = [
    path('',views.home,name='home')
]