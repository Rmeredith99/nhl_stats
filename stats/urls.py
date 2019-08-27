from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('remove_filter/', views.remove_filter_submit, name = 'remove_filter'),
    path('remove_sort/', views.remove_sort_submit, name = 'remove_sort'),
    path('filter_submit/', views.filter_submit, name = 'home_filter'),
    path('metric_submit/', views.metric_submit, name = 'home_metric')
]