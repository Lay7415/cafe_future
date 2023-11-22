from django.urls import path
from . import views

urlpatterns = [
    path('reservation', view=views.reservation_view, name='reservation')
]
