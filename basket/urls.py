from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basketView, name='basket'),
    path('create/<id>/', views.addToBasketView, name='add_to_basket'),
    path('change/<id>/', views.changeBasketFood, name='change_basket'),
    path('basket_food/delete/<int:id>/', views.deleteFromBaksetFood, name='delete_basket_food'),
    path('delete/<int:id>/', views.deleteFromBakset, name='delete_from_basket')
]
