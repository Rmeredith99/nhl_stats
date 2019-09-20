from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    
    path('remove_filter/', views.remove_filter_submit, name = 'remove_filter_empty'),
    path('remove_filter/<str:s>/', views.remove_filter_submit, name = 'remove_filter'),

    path('remove_sort/', views.remove_sort_submit, name = 'remove_sort_empty'),
    path('remove_sort/<str:s>/', views.remove_sort_submit, name = 'remove_sort'),

    path('filter_submit/stats/', views.filter_submit, name = 'home_filter_empty'),
    path('filter_submit/stats/<str:s>/', views.filter_submit, name = 'home_filter'),

    path('metric_submit/stats/', views.metric_submit, name = 'home_metric_empty'),
    path('metric_submit/stats/<str:s>/', views.metric_submit, name = 'home_metric')
]