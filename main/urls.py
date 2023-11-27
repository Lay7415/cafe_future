from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.main_page_view,name='main')
]
