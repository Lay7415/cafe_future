from django.shortcuts import render, redirect
# from django.http import HttpResponseBadRequest
from .forms import RegistrationForm, LoginForm
from .models import User
import secrets
from django.contrib.auth.hashers import make_password, check_password



def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nickname = form.cleaned_data['nickname']
            password = make_password(form.cleaned_data['password'])
            unique_token = secrets.token_hex(16)
            user = User(email=email, password=password, nickname=nickname, unique_token=unique_token)
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
        print(form)
    return render(request, 'access_management/registration.html', {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(
                email=request.POST['email'])
            password = form.cleaned_data['password']
            if not check_password(password, user.password):
                form.add_error(None, 'Invalid email or password.')
            else:
                return redirect('registration')
    else:
        form = LoginForm()
    return render(request, 'access_management/login.html', {'form': form})