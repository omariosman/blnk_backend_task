from django.shortcuts import render, redirect

# Create your views here.

from .models import Loan1
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