from django.contrib import admin
from django.urls import path, include
from map import views

app_name = 'map'

urlpatterns = [
    path('', views.index),
]
