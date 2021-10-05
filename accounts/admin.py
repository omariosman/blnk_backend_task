from django.contrib import admin
from .models import User, Customer, Loan_Provider

# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Loan_Provider)