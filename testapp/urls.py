from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.add_value, name='addition'),
]
