from django.shortcuts import render
from food.models import Food

# Create your views here.
def main_page_view(request):
    foods = Food.objects.all()
    return render(request, 'main/main.html', {"foods": foods})