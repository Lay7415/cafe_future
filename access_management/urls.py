from django.urls import path
from . import views

urlpatterns = [
    path('registration', view=views.registration_view, name='registration'),
    path('login', view=views.login_view, name='login')
]
