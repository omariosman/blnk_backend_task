from django.shortcuts import render, redirect
import numpy_financial as npf

# Create your views here.

from .models import Loan1,Loan_to_Loan_Fund, Loan_Template
from .forms import LoanForm, LoanFundForm
from django.contrib.auth.decorators import login_required

def home_page(request):
    myuser = request.user
    context = {"myuser": myuser}
    return render(request, 'home_page.html', context)

@login_required
def get_loan(request):
    form = request.POST or None
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            #form.user.add(*[request.user]) 
            return redirect('/')
    else:
        form = LoanForm()
    
    context = {
        'form': form
    }
    return render(request, "get_loan.html", context)

@login_required
def loan_fund(request):
    form = request.POST or None
    if request.method == 'POST':
        form = LoanFundForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = LoanFundForm()
    
    context = {
        'form': form
    }
    return render(request, "loan_fund.html", context)

def all_loans(request):
    all_loans=Loan1.objects.all()
    
    context = {

        'all_loans': all_loans
    }
    return render(request, "all_loans.html", context)



def PMT(request):
    instances = Loan_to_Loan_Fund.objects.all()
    #templates= Loan_Template.objects.all()
    #instances = Loan_to_Loan_Fund.objects.all()
    
    loan_amounts=[]
    interest_rates= []
    payements_number= []
    pmt_values = []
    for i in range(len(instances)):
        #print (instances[i].loan.amount)
        loan_amounts.append(instances[i].loan.amount)
        interest_rates.append(Loan_Template.objects.get(type=instances[i].loan.type).interest_rate)
        #print(interest_rates[0])
        payements_number.append(Loan_Template.objects.get(type=instances[i].loan.type).payments_number)
        pmt_values.append(npf.pmt(interest_rates[i],payements_number[i],loan_amounts[i]))
        instances[i].pmt_out=pmt_values[i]
        print(pmt_values[i])
        print(instances[i].pmt_out)
        
    context = {}
    return render(request, "pmt.html", context)
