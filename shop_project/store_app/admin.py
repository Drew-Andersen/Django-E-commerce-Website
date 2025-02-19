from django.contrib import admin
from store_app.models import UserProfileInfo, Category, Customer, Products, Order

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)