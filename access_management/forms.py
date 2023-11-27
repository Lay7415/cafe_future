from django import forms
from django.contrib.auth.forms import UserCreationForm


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


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Email'
    }))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'authorization-field',
        'placeholder': 'Password'
    }))
