from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .form import CustomerSignUpForm, LoanProviderSignUpForm
from .models import User, Customer, Loan_Provider
from django.urls import reverse

# Create your views here.

def register(request):
    return render(request, 'register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "customer_register.html"
    def get_success_url(self):
        return reverse('register')

class loan_provider_register(CreateView):
    model = User
    form_class = LoanProviderSignUpForm
    template_name = "loan_provider_register.html"
    def get_success_url(self):
        return reverse('register')
