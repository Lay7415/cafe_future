from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout



def registration_view(request):
    try:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                login(request, user)
                return redirect('main')
        else:
            form = RegistrationForm()
        
        return render(request, 'access_management/registration.html', {"form": form})
    except Exception as error:
        return HttpResponseBadRequest(error)

def login_view(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                
                user = User.objects.get(email=email)
                
                if check_password(password, user.password):
                    authenticate(request, email=email)
                    login(request, user)
                    return redirect('main')
                
        else:
            form = LoginForm()
        
        return render(request, 'access_management/login.html', {'form': form})
    except Exception as error:
        return HttpResponseBadRequest(error)

def logoutView(request):
    try:
        logout(request)
        return redirect('main')
    except Exception as error:
        return HttpResponseBadRequest(error)