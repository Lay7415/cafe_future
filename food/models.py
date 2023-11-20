from django.db import models

class FoodType(models.Model):
    name = models.CharField(max_length=255)

class Food(models.Model):
    photo = models.ImageField(upload_to='food_photos')
    description = models.TextField()
    composition = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    type_of_food = models.ForeignKey(FoodType, on_delete=models.CASCADE)
