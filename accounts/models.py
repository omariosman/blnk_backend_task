from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#This is inheriting from django user class and extending its fields
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_loan_provider = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance = models.IntegerField(default=0)

class Loan_Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    balance = models.IntegerField(default=0)




