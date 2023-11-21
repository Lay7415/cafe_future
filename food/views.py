from django.shortcuts import render
from .models import Food

# Create your views here.
def catalog_view(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        return render(request, template_name='food/catalog.html', context={"foods": foods})