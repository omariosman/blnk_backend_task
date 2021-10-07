from django.shortcuts import render, redirect
import numpy as np

# Create your views here.

from .models import Loan1,Loan_to_Loan_Fund, Loan_Template
from .forms import LoanForm

def get_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('register')
    else:
        form = LoanForm()
    
    context = {
        'form': form
    }
    return render(request, "get_loan.html", context)


def all_loans(request):
    all_loans=Loan1.objects.all()
    
    context = {

        'all_loans': all_loans
    }
    return render(request, "all_loans.html", context)



def PMT(request):
    instances = Loan_to_Loan_Fund.objects.all()
    templates= Loan_Template.objects.all()
    #instances = Loan_to_Loan_Fund.objects.all()
    
    loan_amounts=[]
    interest_rates= []
    payements_number= []
    for i in len(instances):
        print (instances[i].loan.amount)
        loan_amounts.append(instances[i].loan.amount)
        interest_rates.append(Loan_Template.objects.get(type=instances[0].loan.type).interest_rate)

        
        print(interest_rates[0])