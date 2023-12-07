from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Username'
    }))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Email'
    }))
    first_name = forms.CharField(label='First Name', max_length=30, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(label='Last Name', max_length=30, widget=forms.TextInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Last Name'
    }))
    password1 = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(label='Password checking', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Password checking'
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
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Email'
    }))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Password'
    }))
    
    def clean(self):
        clean_data = super().clean()
        email = clean_data.get('email')
        existing_users = User.objects.filter(email=email)
        if not existing_users.exists():
            self.add_error('email', 'Пользователь с этим Email не существует')
        return clean_data
