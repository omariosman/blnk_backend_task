from django.urls import path
from . import views
urlpatterns = [
    path('get_loan/', views.get_loan, name="get_loan"),
    
]
