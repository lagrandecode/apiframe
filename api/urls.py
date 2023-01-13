from . import views
from django.urls import path

urlpatterns = [
    path('',views.api_list,name='api'),
    path('<int:pk>/',views.api_detail)
]