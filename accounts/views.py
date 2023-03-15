from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'auth/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
