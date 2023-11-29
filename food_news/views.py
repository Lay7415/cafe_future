# cafe_news/views.py
from django.shortcuts import render
from .models import News

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'item-page/news_list.html', {'news_items': news_items})
