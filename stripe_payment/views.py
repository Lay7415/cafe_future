from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from access_management.models import User
from tables.models import Table, ReservedTable
from basket.models import BasketModel, BasketFood
import stripe
from datetime import timedelta

stripe.api_key = "sk_test_51OF9ZiJlUwfLCchq4XPjOfoeqVGIDekaUl8wcvgyhjMMf2M0N8JspYGUwiLTLUAEkemHlaZdahWw97RFeZEk8TI200q5nhJawS"


def stripePay_basket(request, email):
    if request.method == "POST":
        amount = int(request.POST["amount"])
        try:
            customer = stripe.Customer.create(
                email=request.POST.get("email"),
                name=request.POST.get("full_name"),
                description="Test donation",
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            return HttpResponse("<h1>Произошла ошибка при списании средств с вашей карты:</h1>" + str(e))

        except stripe.error.RateLimitError as e:
            return HttpResponse("<h1>Ошибка на лимит запроса!</h1>")

        except stripe.error.InvalidRequestError as e:
            return HttpResponse("<h1>Ошибка транзакции!</h1>")

        except stripe.error.AuthenticationError as e:
            return HttpResponse("<h1>Недопустимый аутентификатор API ключа!</h1>")

        except stripe.error.StripeError as e:
            return HttpResponse("<h1>Stripe Ошибка!</h1>")

        except Exception as e:
            pass

        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount) * 100,
            currency='usd',
            description="Test donation"
        )
        transRetrive = stripe.Charge.retrieve(
            charge["id"],
            api_key="sk_test_51OF9ZiJlUwfLCchq4XPjOfoeqVGIDekaUl8wcvgyhjMMf2M0N8JspYGUwiLTLUAEkemHlaZdahWw97RFeZEk8TI200q5nhJawS"
        )
        charge.save()  # Использует тот же ключ API.
        return redirect("stripe/pay_success/")
    
    user = User.objects.get(email=email)
    print(user.first_name)
    basket = BasketModel.objects.get(user=user)
    basket_foods = BasketFood.objects.filter(basket=basket)
    amount_value = 0
    for item in basket_foods:
        amount_value += item.food.price
    context = {"amount_value": amount_value, "email": email, "fullname": f'{user.first_name} {user.last_name}'}
    return render(request, "stripe_payment/index.html", context)


def stripePay_reserved_table(request, table_id, date, email):
    if request.method == "POST":
        amount = int(request.POST["amount"])
        try:
            customer = stripe.Customer.create(
                email=request.POST.get("email"),
                name=request.POST.get("full_name"),
                description="Test donation",
                source=request.POST['stripeToken']
            )
        except stripe.error.CardError as e:
            return HttpResponse("<h1>Произошла ошибка при списании средств с вашей карты:</h1>" + str(e))

        except stripe.error.RateLimitError as e:
            return HttpResponse("<h1>Ошибка на лимит запроса!</h1>")

        except stripe.error.InvalidRequestError as e:
            return HttpResponse("<h1>Ошибка транзакции!</h1>")

        except stripe.error.AuthenticationError as e:
            return HttpResponse("<h1>Недопустимый аутентификатор API ключа!</h1>")

        except stripe.error.StripeError as e:
            return HttpResponse("<h1>Stripe Ошибка!</h1>")

        except Exception as e:
            pass

        charge = stripe.Charge.create(
            customer=customer,
            amount=int(amount) * 100,
            currency='usd',
            description="Test donation"
        )
        transRetrive = stripe.Charge.retrieve(
            charge["id"],
            api_key="sk_test_51OF9ZiJlUwfLCchq4XPjOfoeqVGIDekaUl8wcvgyhjMMf2M0N8JspYGUwiLTLUAEkemHlaZdahWw97RFeZEk8TI200q5nhJawS"
        )
        charge.save()  # Использует тот же ключ API.
        table = Table.objects.get(id=table_id)
        user = User.objects.get(email=email)
        print(date)
        duration = timedelta(hours=2)
        reserved_table = ReservedTable.objects.create(user=user, table=table, data=date, duration=duration)
        url = reverse('reserved', args=[table_id])
        return redirect(url)    
    user = User.objects.get(email=email)
    table = Table.objects.get(id=table_id)
    
    context = {"amount_value": int(table.price), "email": email, "fullname": f'{user.first_name} {user.last_name}'}
    return render(request, "stripe_payment/index.html", context)


def paysuccess(request):
    return render(request, "stripe_payment/success.html")
