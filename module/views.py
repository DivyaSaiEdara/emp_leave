from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.models import *
def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None :
            auth.login(request,user)
            return render(request,'homepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


from django.contrib.auth.models import User


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']  # New first name field
        last_name = request.POST['last_name']  # New last name field
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username already taken')
                return render(request, 'signup.html')
            else:
                # Create the user with username, email, password, first name, and last name
                user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Passwords do not match')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')


def newhomepage(request):
    return render(request,'newhomepage.html')
def homepage(request):
    return render(request,'homepage.html')
def hr_homepage(request):
    return render(request,'hr_homepage.html')

