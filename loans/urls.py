from django.urls import path
from . import views
urlpatterns = [
    path('get_loan/', views.get_loan, name="get_loan"),
     path('all_loans/', views.all_loans, name="all_loans"),
          path('pmt/', views.PMT, name="pmt"),

]
