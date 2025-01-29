from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

###################################################################################################################################################3
#HOME PAGE
#Function for home page
def home(request):
    if request.user.is_anonymous:
        return redirect('landing_page')
    return render(request,'home.html')

#open/close slider
def slider(request):
    slider_value = 0  # This can be dynamically set from the backend
    return render(request, 'slider.html', {'slider_value': slider_value})

###################################################################################################################################################3
#REGISTER N LOGIN PAGE
#Function for reh_login page   
def landing_page(request):
    return render(request,"landing_page.html")

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

###################################################################################################################################################3
#OFFERS
def offers(request):
    return render(request,'offers.html')

###################################################################################################################################################
#CART
def cart(request):
    return render(request,'cart.html')

###################################################################################################################################################
#MENU
def menu(request):
    return render(request,'menu.html')

###################################################################################################################################################
#OFFERS
def order_tracking(request):
    return render(request,'order_tracking.html')

###################################################################################################################################################
