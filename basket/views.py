from django.shortcuts import render
from django.http import JsonResponse
from .models import BasketModel, BasketFood
from food.models import Food
from access_management.models import User
import json


def basketView(request):
    user_id = request.user.id
    if user_id is not None:
        user = User.objects.get(id=user_id)
        basket = BasketModel.objects.get(user=user)
        foods = BasketFood.objects.filter(basket=basket)
        total_quantity = 0
        total_amount = 0
        for food in foods:
            print(type(food.amount))
            total_amount += food.amount
            total_quantity += food.quantity
        context = {"foods": foods, 'auth': user_id,
                   "total_quantity": total_quantity, "total_amount": total_amount}
        return render(request, 'basket/index.html', context)


def addToBasketView(request, id):
    print(id)
    user_id = request.user.id
    if user_id is not None:
        newuser = User.objects.get(id=user_id)
        basket = BasketModel.objects.get(user=newuser)
        food = Food.objects.get(id=id)
        BasketFood.objects.create(
            basket=basket, food=food, quantity=1, amount=int(food.price))

        return JsonResponse({"message": 'ok'})


def changeBasketFood(request, id):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        foodId = int(id)
        quantity = int(json_data["quantity"])
        price = int(float(json_data["price"]))
        BasketFood.objects.filter(id=foodId).update(
            quantity=quantity, amount=price)

        return JsonResponse({"message": 'ok'})
