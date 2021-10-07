from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Customer, Loan_Provider
from django.db import transaction




class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    balance = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)    
        user.is_customer = True   
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.balance = self.cleaned_data.get('balance')
        customer.save()
        return customer


class LoanProviderSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    balance = forms.IntegerField()

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_loan_provider = True
        
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        loan_provider = Loan_Provider.objects.create(user=user)
        loan_provider.balance = self.cleaned_data.get('balance')
        loan_provider.save()
        return loan_provider

