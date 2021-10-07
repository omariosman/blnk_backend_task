from django.urls import path
from . import views
from django.contrib.auth import authenticate, login
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('customer_register/', views.customer_register.as_view(), name="customer_register"),
    path('loan_provider_register/', views.loan_provider_register.as_view(), name="loan_provider_register"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('signout/',views.signout, name="signout")

]
