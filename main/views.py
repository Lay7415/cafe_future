from django.shortcuts import render
from .forms import FoodFilterForm
from food.models import Food
from basket.models import BasketFood, BasketModel
from access_management.models import User

def main_page_view(request):
<<<<<<< HEAD
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
=======
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
>>>>>>> 3c1d8acda4776110f663b347b92731bf611d5a23
