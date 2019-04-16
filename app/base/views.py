from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'base/home.html')


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect(reverse('home'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/registration.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'registration/profile.html', {'form': form})


@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()

        return redirect(reverse('home'))

    return render(request, 'registration/profile_delete.html')


def logout_view(request):
    logout(request)
    return render(request, 'registration/logout.html')