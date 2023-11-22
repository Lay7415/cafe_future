from django.shortcuts import render
from .forms import FoodFilterForm
from .models import Food


def catalog_view(request):
    form = FoodFilterForm(request.GET)
    foods = Food.objects.all()

    if form.is_valid():
        type_of_food = form.cleaned_data['type_of_food']
        min_price = form.cleaned_data['min_price']
        max_price = form.cleaned_data['max_price']
        search_query = form.cleaned_data['search_query'].lower()

        if type_of_food:
            foods = foods.filter(type_of_food=type_of_food)

        if min_price is not None:
            foods = foods.filter(price__gte=min_price)

        if max_price is not None:
            foods = foods.filter(price__lte=max_price)

        if search_query:
            search_results = []
            for food in foods:
                if search_query in food.name.lower():
                    search_results.append(food)

            foods = search_results

    return render(request, 'food/catalog.html', {'form': form, 'foods': foods})