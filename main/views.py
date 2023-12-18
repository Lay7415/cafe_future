from django.shortcuts import render
from .forms import FoodFilterForm
from food.models import Food
from basket.models import BasketFood, BasketModel
from access_management.models import User
from .forms import FoodFilterForm

def main_page_view(request):
    auth = request.user.id
    form = FoodFilterForm(request.GET)
    if auth is None:
        if form.is_valid():
            foods = Food.objects.all()
            searchFoods = Food.objects.all()
            search_query = form.cleaned_data['search_query'].lower()
            if search_query != '':
                search_results = []
                for food in searchFoods:
                    if search_query in food.name.lower():
                        search_results.append(food)

                searchFoods = search_results
            else:
                searchFoods = []
        return render(request, 'main/main.html', {'form': form, 'foods': foods, 'searchFoods': searchFoods, 'auth': auth})
    else:
        if form.is_valid():
            searchFoods = Food.objects.all()
            search_query = form.cleaned_data['search_query'].lower()
            if search_query != '':
                search_results = []
                for food in searchFoods:
                    if search_query in food.name.lower():
                        search_results.append(food)

                searchFoods = search_results
            else:
                searchFoods = []
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
            return render(request, 'main/main.html', {'form': form, "foods": filteredFoods, 'auth': auth, 'searchFoods': searchFoods, 'auth': auth})


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