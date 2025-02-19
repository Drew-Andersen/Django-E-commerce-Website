from django.contrib import admin
from django.urls import path
from store_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
]