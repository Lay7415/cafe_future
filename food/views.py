from django.shortcuts import render, get_object_or_404
from .forms import FoodFilterForm
from .models import Food
from basket.models import BasketFood, BasketModel
from access_management.models import User
from django.http import HttpResponseBadRequest


def catalog_view(request):
    try:
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
                basketId = BasketFood.objects.filter(
                    basket=basket).values_list('food', flat=True)
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
    except Exception as error:
        return HttpResponseBadRequest(error)


def food_detail_view(request, food_id):
    try:
        if request.user.is_authenticated:
            user = get_object_or_404(User, id=request.user.id)
            basket, created = BasketModel.objects.get_or_create(user=user)
        else:
            user = None
            basket = None

        found_food = get_object_or_404(Food, id=food_id)
        try:
            # Try to get the BasketFood object
            in_basket = BasketFood.objects.get(food=found_food, basket=basket)
            in_basket = True
        except BasketFood.DoesNotExist:
            # BasketFood object not found
            in_basket = False
                 
        food_details = {
            "id": found_food.id,
            "photo": found_food.photo,
            "name": found_food.name,
            "composition": found_food.composition,
            "price": found_food.price,
            "type_of_food": found_food.type_of_food,
            "inBasket": in_basket
        }

        return render(request, 'food/food_detail.html', {'food': food_details, 'auth': user.id if user else None})

    except Exception as error:
        # Handle exceptions and return a meaningful response
        return HttpResponseBadRequest(f"Error: {error}")

