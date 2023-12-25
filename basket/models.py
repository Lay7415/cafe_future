from django.db import models
from access_management.models import User
from food.models import Food

class BasketModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Корзинка'
        verbose_name_plural = 'Корзинки'
        
    def calculate_total_amount(self):
        foods = self.basketfood_set.all()
        total_amount = sum(food.calculate_amount() for food in foods)
        return total_amount
    
class BasketFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Еда')
    quantity = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()
    basket = models.ForeignKey(BasketModel, on_delete=models.CASCADE, verbose_name='Корзинка')

    def __str__(self):
        return self.basket.user.email + '---' + self.food.name

    class Meta:
        verbose_name = 'Еда в корзинке'
        verbose_name_plural = 'Еда в корзинке'
