from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *


def users_register(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect("home_app:home")
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if username and email and password1 and password2:
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        pass_verify = password1 != password2
        email_verify = not '@' in email
        if user:
            context['errors'].append('in name karbari ghablan sabt shode ast')
        if pass_verify:
            context['errors'].append('password ha yeksan nistand')
        if email_verify:
            context['errors'].append('email namotabar mibashad')
        if user or pass_verify or email_verify:
            return render(request, 'accounts_app/register.html', context)
        else:
            User.objects.create(username=username, password=password1, email=email)
            return redirect("home_app:home")
    else:
        return render(request, 'accounts_app/register.html', context)


def users_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')
    else:
        form = LoginForm()
    return render(request, 'accounts_app/login.html', context={'form':form})
            
            
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(request, username=username, password=password)
    # if user:
    #     login(request, user)
    #     return redirect("home_app:home")
    # else:
    #     return render(request, 'accounts_app/login.html', context={})


def users_logout(request):
    logout(request)
    return redirect("home_app:home")


def user_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app:home')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'accounts_app/edit.html', context={'form':form})
