from django.shortcuts import render
from .forms import FoodFilterForm
from food.models import Food

# Create your views here.
def main_page_view(request):
    form = FoodFilterForm(request.GET)
    foods = Food.objects.all()
    searchFoods = Food.objects.all()


    if form.is_valid():
        search_query = form.cleaned_data['search_query'].lower()
        if search_query != '':
            search_results = []
            for food in searchFoods:
                if search_query in food.name.lower():
                    search_results.append(food)

            searchFoods = search_results
        else:
            searchFoods = []
    return render(request, 'main/main.html', {'form': form, 'foods': foods, 'searchFoods': searchFoods})
