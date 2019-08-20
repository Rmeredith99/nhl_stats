from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str: url_string>/', views.home, name = 'home_filter'),
]