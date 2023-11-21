from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'access_management/registration.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.get(email=email)
            
            if user.check_password(password):
                authenticate(request, email=email)
                login(request, user)
                return redirect('registration')
            
    else:
        form = LoginForm()
    
    return render(request, 'access_management/login.html', {'form': form})