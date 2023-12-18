from django.shortcuts import render
from .forms import FoodFilterForm
from food.models import Food
from basket.models import BasketFood, BasketModel
from access_management.models import User

def main_page_view(request):
    auth = request.user.id
    if auth is None:
        foods = Food.objects.all()
        return render(request, 'main/main.html', {"foods": foods, 'auth': auth})
    else:
        user = User.objects.get(id=auth)
        basket, another = BasketModel.objects.get_or_create(user=user)
        basketId = BasketFood.objects.filter(basket=basket).values_list('food', flat=True)
        foods = list(Food.objects.all())
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

        return render(request, 'main/main.html', {"foods": filteredFoods, 'auth': auth})
