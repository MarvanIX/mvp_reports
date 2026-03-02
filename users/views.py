from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'users/login.html')

def user_register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('users/register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('users/register')

        user = User.objects.create_user(
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'users/register')
