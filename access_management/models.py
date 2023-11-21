from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100, verbose_name='Электронная почта')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    username = models.CharField(unique=True, max_length=100, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'