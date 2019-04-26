from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

# Sign up and register a new user 
def Signup(request):
    # If the request is post the user wants to be registered
    if request.method == 'POST':
        # Check if both password fields are correct
        if request.POST['password1'] == request.POST['password2']:
            try:
     # Check if the user exists also check if the user name is already taken if taken return an error on same page
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username is already taken.'})
            except User.DoesNotExist: #If the user doesnot exists create a new user 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('login')
        else: # Password doesnot match
            return render(request, 'accounts/signup.html', {'error':'Password doesnot match'})
    else: # The request is GET
        return render(request, 'accounts/signup.html')


# Log in   if log in succeeds send the user to home page
def Login(request):
    if request.method == 'POST':
        #check if the user exists in the User model and if yes authenticate
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
        # Check if user is in model table
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: #user is not in model
            return render(request, 'accounts/login.html', {'error':'Username or Password doesnot match.'})
    else:
        return render(request, 'accounts/login.html')


# Log out the user 
def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    else:
        return render(request, 'accounts/login.html')
