from django.db import models

class FoodType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип еды'
        verbose_name_plural = 'Типы еды'

class Food(models.Model):
    photo = models.ImageField(upload_to='food_photos', verbose_name='Фотография')
    name = models.TextField(max_length=255, verbose_name='Название')
    composition = models.TextField(verbose_name='Состав')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    type_of_food = models.ForeignKey(FoodType, on_delete=models.CASCADE, verbose_name='Тип еды')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'