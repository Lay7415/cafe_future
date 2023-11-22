from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Имя пользователя'
    }))
    email = forms.EmailField(label='Электронная почта', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Электронная почта'
    }))
    first_name = forms.CharField(label='Имя', max_length=30, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Имя'
    }))
    last_name = forms.CharField(label='Фамилия', max_length=30, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Фамилия'
    }))
    password1 = forms.CharField(label='Пароль', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(label='Подтверждение пароля', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Подтверждение пароля'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {
            'unique': 'Пользователь с таким именем уже существует.'}
        self.fields['email'].error_messages = {
            'unique': 'Пользователь с таким Email уже существует.'}
        self.fields['password2'].error_messages = {
            'password_mismatch': 'Пароли не совпадают.'}


class LoginForm(forms.Form):
    email = forms.EmailField(label='Электронная почта', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Электронная почта'
    }))
    password = forms.CharField(label='Пароль', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Пароль'
    }))

    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        existing_users = User.objects.filter(email=email)
        if not existing_users.exists():
            self.add_error('email', 'Пользователь с этим Email не существует')
        return clean_data
