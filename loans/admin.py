from django.contrib import admin
from .models import Loan_Template,Loan1, Loan_Fund, Loan_to_Loan_Fund
# Register your models here.
admin.site.register(Loan_Template)
admin.site.register(Loan1)
admin.site.register(Loan_Fund)
admin.site.register(Loan_to_Loan_Fund)