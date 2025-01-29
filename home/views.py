from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

#Function for home page
def home(request):
    if request.user.is_anonymous:
        return redirect('reg_login')
    return render(request,'home.html')

#Function for reh_login page   
def reg_login(request):
    return render(request,"reg_login.html")

#Function for login page
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            # messages.error(request,'Invalid username or password')
            return render(request,'login.html',{'error':"Invalid username or password"})
    return render(request,'login.html')

#Function for registeration page
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists:
                return render(request,'register.html',{'error':"Email already exists"})
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                return redirect("login")
    else:
        return render(request,'register.html',{'error':"Passwords do not match"})
    return render(request,'register.html')

