from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . models import Customer
from django.contrib import messages
# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('home')

def account(request):
    try:
        if request.POST and 'register' in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            customer=Customer.objects.create(
                name=username,
                user=user,
                address=address,
                phone=phone,
            )
            success="Registration successful"
            messages.success(request,success)
    except Exception as e:
        error_message="Duplicate user or invalid input!"
        messages.error(request,error_message)
    try:
        if request.POST and 'login' in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                error_message="Invalid username or password!"
                messages.error(request,error_message)
    except Exception as e:
        error_message="Invalid username or password!"
        messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
    return render(request,'account.html')
