from django import forms
from .models import Loan1, Loan_Fund

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan1
        fields = ['amount', 'type', 'date']

class LoanFundForm(forms.ModelForm):
    class Meta:
        model = Loan_Fund
        fields = ['amount', 'type', 'date']
    