from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import ElectricCarDir
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def index(request):
    projects = ElectricCarDir.objects.all()
    return render(request, 'electric_car_dir/index.html', {'projects': projects})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def profile(request):
    return render(request, 'electric_car_dir/profile.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'electric_car_dir/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'electric_car_dir/loginuser.html', {'form': AuthenticationForm(), 'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect('profile')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'electric_car_dir/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'electric_car_dir/signupuser.html',
                              {'form': UserCreationForm(), 'error': 'Такой логин уже существует'})
        else:
            return render(request, 'electric_car_dir/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Пароли не совпадают'})


