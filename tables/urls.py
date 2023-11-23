from django.urls import path
from . import views

urlpatterns = [
    path('tables/', view=views.tables_view, name='tables')
]
