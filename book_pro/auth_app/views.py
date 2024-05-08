
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.

def Register_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'this user name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This mail already taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
            return redirect('login')

        else:
            messages.info(request, 'This password not matching')
            return redirect('register')

    return render(request, 'authen/register.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'please provide correct details ')
            return redirect('login')


    return render(request, 'authen/login.html')


def logOut(request):
    auth.logout(request)
    return redirect('login')