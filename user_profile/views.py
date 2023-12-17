from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib import messages

def view_profile(request):
    user_profile = request.user.userprofile if hasattr(request.user, 'userprofile') else None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            if user_profile:
                form.save()
            else:
                new_profile = form.save(commit=False)
                new_profile.user = request.user
                new_profile.save()
            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user_profile/profile.html', {'form': form})