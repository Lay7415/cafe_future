from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basketView, name='basket'),
    path('create/<id>/', views.addToBasketView, name='add_to_basket'),
    path('change/<id>/', views.changeBasketFood, name='change_basket'),
]
