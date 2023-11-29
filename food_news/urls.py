# cafe_news/urls.py
from django.urls import path
from .views import news_list

urlpatterns = [
        path('food_news/', news_list, name='news_list'),
    # Добавьте другие URL-маршруты при необходимости
]
