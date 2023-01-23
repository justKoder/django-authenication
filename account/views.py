from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def homepage(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('<h1>Password mismatch</h1>')

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return HttpResponse("<h1>Something Went Wrong</h1>")
    return render(request, 'login.html')


def register_user(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse('<h1>Password mismatch</h1>')

        hashed_password = make_password(password1)

        User.objects.create(first_name=firstname, last_name=lastname,
                            username=username, email=email, password=hashed_password)

        return HttpResponse("<h1>Welcome To Our Family</h>")
    return render(request, 'register.html')


def logout_user(request):
    logout(request)
    return redirect('register')
