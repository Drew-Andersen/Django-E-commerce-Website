from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    # save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email): 
        try: 
            return Customer.objects.get(email=email) 
        except: 
            return False
  
    def isExists(self): 
        if Customer.objects.filter(email=self.email): 
            return True
  
        return False
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=256, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_category(category_id):
        if category_id:
            return Products.objects.filter(category= category_id)
        else:
            return Products.get_all_products()

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.PositiveBigIntegerField(default=1)
    address = models.CharField(max_length=256, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username