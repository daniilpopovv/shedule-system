from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm


def user_login(request):
    if request.method == 'POST':
        auth_form = UserLoginForm(data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            login(request, user)
            return redirect('timesheet')
    else:
        auth_form = UserLoginForm()

    if request.user.is_authenticated:
        return redirect('timesheet')

    return render(request, 'auth/login.html', {'auth_form': auth_form})


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return redirect('login')
