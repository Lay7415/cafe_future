from django.urls import path
from . import views

urlpatterns = [
    path('catalog', view=views.catalog_view, name='catalog'),
    # path('food/<int:food_id>/', view=views.food_detail_view, name='food_detail'),
]
