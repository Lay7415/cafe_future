from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100, verbose_name='Электронная почта')
    username = models.CharField(unique=True, max_length=100, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    password1 = models.CharField(max_length=30, verbose_name='Пароль1')
    password2 = models.CharField(max_length=30, verbose_name='Пароль2')

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
