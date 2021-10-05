from django import forms
from .models import Loan1

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan1
        fields = ['amount', 'type', 'date']
    