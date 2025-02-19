from django.contrib import admin
from django.urls import path
from store_app import views

app_name = 'store_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]