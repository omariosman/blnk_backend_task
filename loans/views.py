from django.shortcuts import render

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
    else:
        form = LoanForm()
    
    context = {
        'form': form
    }
    return render(request, "get_loan.html", context)

