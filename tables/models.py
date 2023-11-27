from django.db import models
from access_management.models import User

class Table(models.Model):
    photo = models.ImageField(upload_to='table_photos', verbose_name='Фотография')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    table_number = models.PositiveIntegerField(verbose_name='Номер Столика')
    type_choices = [
        ('just', 'Just'),
        ('vip', 'VIP'),
        ('booths', 'Booths')
    ]
    type = models.CharField(max_length=20,choices=type_choices, verbose_name='Тип')
    
    def __str__(self):
        return f'{self.table_number}'
    
    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

class ReservedTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Стол')
    data = models.DateTimeField(verbose_name='Дата')
    duration = models.DurationField(verbose_name='Продолжительность')

    def __str__(self):
        return f"Бронь №{self.id} для {self.user} на стол {self.table} на {self.data}"
    
    class Meta:
        verbose_name = 'Бронированный стол'
        verbose_name_plural = 'Бронированные столы'
        
    def get_absolute_url(self):
        return f'/reserved/{self.id}'
