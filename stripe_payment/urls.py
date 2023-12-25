from django.urls import path
from . import views

urlpatterns = [
    path('stripe/basket/<str:table_place>/<str:email>/', views.stripePay_basket, name="stripe_basket"),
    path('stripe/table/<int:table_id>/<date>/<str:email>/', views.stripePay_reserved_table, name="stripe_reserved_table"),
    path('stripe/pay_success/', views.paysuccess, name="success_page"),
]

