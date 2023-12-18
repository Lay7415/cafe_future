from django.urls import path
from .views import stripePay, paysuccess

urlpatterns = [
    path('stripe/', stripePay, name="stripe"),
    path('stripe/pay_success/', paysuccess, name="success_page"),
]

