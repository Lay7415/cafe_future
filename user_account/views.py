from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import AnonymousUser
from .forms import CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def my_account(request):
    if not isinstance(request.user, AnonymousUser):
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('my_account')
        else:
            form = CustomUserChangeForm(instance=request.user)
        return render(request, 'user_account/user_account.html', {'form': form})
    else:
        # Обработка для анонимного пользователя, например, перенаправление на страницу входа
        return redirect('login')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('my_account')  # Замените 'profile' на имя вашего URL-пути для профиля
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'user_account/change_password.html', {'form': form})