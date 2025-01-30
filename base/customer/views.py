from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    if request.user.is_authenticated:  # Use is_authenticated instead of is_anonymous
        return redirect('login')
    return render(request, 'landing.html')


# View for signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        # Check if passwords match
        if password == confirm_password:
            try:
                # Create the user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Signup successful! You can now log in.')
                return render(request,'landing.html')  # Redirect to the login page
            except Exception as e:
            # Print the error message to the console
                print(f"Error during signup: {e}")
                messages.error(request, 'An error occurred during signup. Please try again.')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'landing.html')


# View for login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return render(request, 'home.html')  # Redirect to home or dashboard
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, 'landing.html')
    return render(request, 'landing.html')

