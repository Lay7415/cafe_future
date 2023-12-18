from django.shortcuts import render
from .forms import FoodFilterForm
from .models import Food
from basket.models import BasketFood, BasketModel
from access_management.models import User


def catalog_view(request):
    form = FoodFilterForm(request.GET)
    foods = Food.objects.all()
    auth = request.user.id
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

        if auth is not None:
            user = User.objects.get(id=auth)
            basket, another = BasketModel.objects.get_or_create(user=user)
            basketId = BasketFood.objects.filter(basket=basket).values_list('food', flat=True)
            filteredFoods = []
            for food in foods:
                in_basket = food.id in basketId
                filteredFoods.append({
                    "id": food.id,
                    "name": food.name,
                    "composition": food.composition,
                    "price": food.price,
                    "type_of_food": food.type_of_food.name,
                    "photo": food.photo,
                    "inBasket": in_basket
                })
            return render(request, 'food/catalog.html', {'form': form, 'foods': filteredFoods, 'auth': auth})

        return render(request, 'food/catalog.html', {'form': form, 'foods': foods, 'auth': auth})
