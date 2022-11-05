import imp
from wsgiref.validate import validator
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
# Create your views here.

def Home_page(request):
    return render(request, 'pass_ver_sys/Home.html', {})


def Register_page(request):
    if request.method == 'POST':
        F_name = request.POST.get('First_name')
        L_name = request.POST.get('Last_name')
        email = request.POST.get('Email')        
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        cpassword = request.POST.get('CPassword')
        validate_email(email)
        if(cpassword==password):
            validate_password(password)
            new_user = User.objects.create_user(username,email,password)
            new_user.first_name = F_name
            new_user.last_name = L_name
            new_user.save()
            return redirect('Login')
        else:
            return HttpResponse('Confirm Password does not match the Password entered.')    

    return render(request, 'pass_ver_sys/Register.html', {})

def Login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('Username')
        pwd = request.POST.get('Password')

        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
        else:
            return HttpResponse('Error user does not exist, pls check your login credentials and try again')

    return render(request, 'pass_ver_sys/Login.html', {})

@login_required
def Dashboard_page(request):
    return render(request, 'pass_ver_sys/Dashboard.html', {})

def Logout_page(request):
    logout(request)
    return redirect('Login')

def Admin_page(request):
    return render(request, 'http://127.0.0.1:8000/admin/login/?next=/admin/', {})