from django.urls import path
from . import views

urlpatterns = [
    path('catalog', view=views.catalog_view, name='catalog')
]
