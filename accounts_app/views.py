from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def users_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'accounts_app/login.html', context={})


def users_logout(request):
    logout(request)
    return redirect('/')

