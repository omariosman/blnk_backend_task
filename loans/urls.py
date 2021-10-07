from django.urls import path
from . import views

app_name='loans'

urlpatterns = [
    path('get_loan/', views.get_loan, name="get_loan"),
    path('loan_fund/', views.loan_fund, name="loan_fund"),
     path('all_loans/', views.all_loans, name="all_loans"),
          path('pmt/', views.PMT, name="pmt"),
    path('', views.home_page, name="home_page"),
]

