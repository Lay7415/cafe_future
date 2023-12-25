from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from access_management.models import User

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User  # Замените User на вашу модель пользователя, если вы используете другую
