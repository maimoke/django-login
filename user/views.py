from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .form import RegisterForm


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@login_required(login_url="/sign-in")
def home(request):
    # sign user out
    print(request)
    if request.method == "get":
        logout(request)
        return redirect(request, 'user/sign-in.html')

    # Redirect to sign-in page
    return render(request, 'user/home.html')

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
            return redirect('/user/home')
            
    return render(request, 'user/sign-in.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/user/home')
    else:
        form = RegisterForm()
        print(form)

    return render(request, 'user/sign-up.html', {'form': form})