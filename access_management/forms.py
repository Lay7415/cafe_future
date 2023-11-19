from typing import Any
from django import forms
from .models import User


class RegistrationForm(forms.Form):
    nickname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'nickname'
    }))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'password'
    }))
    password_check = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'password'
    }))

    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        password = clean_data.get('password')
        password_check = clean_data.get('password_check')
        existing_users = User.objects.filter(email=email)
        if existing_users.exists():
            self.add_error('email', 'Email уже существует')
        if password != password_check:
            self.add_error('password_check', 'Пароли не совпадают')
        return clean_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Email'
    }))
    password = forms.CharField(max_length=8, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'password'
    }))
    
    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        existing_users = User.objects.filter(email=email)
        if not existing_users.exists():
            self.add_error('email', 'Email не существует')
        return clean_data
