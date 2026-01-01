from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .form import RegisterForm



@login_required
def index(request):
    return render(request, 'user/index.html')

def sign_out(request):
    logout(request)
    return redirect('/user')
    
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request, 
            username=username, 
            password=password
        )
        print(user)
        print(username)
        print(password)
        if user is not None:
            # Log user in
            login(request, user)
            return redirect('/user/')
            
    return render(request, 'user/sign-in.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/user/')
    else:
        form = RegisterForm()
        print(form)

    return render(request, 'user/sign-up.html', {'form': form})
