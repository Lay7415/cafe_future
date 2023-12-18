from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from .models import BasketModel, BasketFood
from food.models import Food
from access_management.models import User
import json


def basketView(request):
    try:
        user_id = request.user.id
        if user_id is not None:
            user = User.objects.get(id=user_id)
            basket = BasketModel.objects.get(user=user)
            foods = BasketFood.objects.filter(basket=basket)
            total_quantity = 0
            total_amount = 0
            for food in foods:
                total_amount += food.amount
                total_quantity += food.quantity
            context = {"foods": foods, 'auth': user_id,
                       "total_quantity": total_quantity, "total_amount": total_amount, "basket": basket}
            return render(request, 'basket/index.html', context)
    except Exception as error:
        return HttpResponseBadRequest(error)


def addToBasketView(request, id):
    try:
        user_id = request.user.id
        if user_id is not None:
            newuser = User.objects.get(id=user_id)
            basket = BasketModel.objects.get(user=newuser)
            food = Food.objects.get(id=id)
            BasketFood.objects.create(
                basket=basket, food=food, quantity=1, amount=int(food.price))

            return JsonResponse({"message": 'ok'})
    except Exception as error:
        return HttpResponseBadRequest(error)


def changeBasketFood(request, id):
    try:
        user_id = request.user.id
        if request.method == 'POST':
            json_data = json.loads(request.body)
            foodId = int(id)
            newuser = User.objects.get(id=user_id)
            basket = BasketModel.objects.get(user=newuser)
            quantity = int(json_data["quantity"])
            price = int(float(json_data["price"]))
            BasketFood.objects.filter(basket=basket, id=foodId).update(
                quantity=quantity, amount=price)

            return JsonResponse({"message": 'ok'})
    except Exception as error:
        return HttpResponseBadRequest(error)


def deleteFromBaksetFood(request, id):
    try:
        user_id = request.user.id
        newuser = User.objects.get(id=user_id)
        basket = BasketModel.objects.get(user=newuser)
        food = Food.objects.get(id=id)
        basketFood = BasketFood.objects.get(food=food, basket=basket)
        basketFood.delete()
        return JsonResponse({"message": 'ok'})
    except Exception as error:
        return HttpResponseBadRequest(error)

def deleteFromBakset(request, id):
    try:
        user_id = request.user.id
        newuser = User.objects.get(id=user_id)
        basket = BasketModel.objects.get(user=newuser)
        basketFood = BasketFood.objects.get(id=id, basket=basket)
        basketFood.delete()
        return JsonResponse({"message": 'ok'})
    except Exception as error:
        return HttpResponseBadRequest(error)
