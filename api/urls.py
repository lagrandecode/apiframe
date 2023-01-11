from . import views
from django.urls import path

urlpatterns = [
    path('snip/',views.api_list,name='api'),
    path('snip/<int:pk>/',views.api_detail)
]