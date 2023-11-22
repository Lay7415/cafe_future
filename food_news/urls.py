# cafe_news/urls.py
from django.urls import path
from .views import news_list

urlpatterns = [
    path('news/', news_list, name='news_list'),
]
