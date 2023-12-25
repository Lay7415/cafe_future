from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.my_account, name='my_account'),
    path('change_password/', views.change_password, name='change_password'),

]
