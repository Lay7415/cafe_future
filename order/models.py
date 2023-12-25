from django.db import models
from access_management.models import User

class OrderOfFoodModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Пользователь")
    place = models.TextField(max_length=200, verbose_name='Место')
    amount = models.PositiveIntegerField()
    products = models.TextField(verbose_name="продукты")
    
    def __str__(self):
        return f"{self.user.email }{self.place}"
    
    class Meta:
        verbose_name = 'Заказ еды'
        verbose_name_plural = 'Заказы еды'