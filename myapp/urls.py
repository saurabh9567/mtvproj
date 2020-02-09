from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ind1/', views.index1),
]