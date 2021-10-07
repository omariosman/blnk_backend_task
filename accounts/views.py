from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .form import CustomerSignUpForm, LoanProviderSignUpForm
from .models import User, Customer, Loan_Provider
from django.urls import reverse, reverse_lazy

from django.contrib.auth import logout




# Create your views here.

def register(request):
    return render(request, 'register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "customer_register.html"
    def get_success_url(self):
        return reverse('loans:home_page')

class loan_provider_register(CreateView):
    model = User
    form_class = LoanProviderSignUpForm
    template_name = "loan_provider_register.html"
    def get_success_url(self):
        return reverse('loans:home_page')



def signout(request):
    logout(request)
    context = {}
    return render(request, "logout.html", context)
