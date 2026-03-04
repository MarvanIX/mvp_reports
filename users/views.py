from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from reports.models import Company

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
    companies = Company.objects.all() 

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        company_id = request.POST.get('company') 

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('users/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('users/register.html')

        user = User.objects.create_user(
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )

        if company_id:
            company = get_object_or_404(Company, id=company_id)
            company.managers.add(user)

        login(request, user)
        return redirect('home')

    return render(request, 'users/register.html', {'companies': companies})