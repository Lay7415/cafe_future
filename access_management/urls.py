from django.urls import path
from . import views

urlpatterns = [
    path('registration', views.registration_view, name='registration'),
    path('login', views.login_view, name='login')
]
