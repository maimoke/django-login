from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from .form import RegisterForm


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def sign_out(request):
    # sign user out
    logout(request)

    # Redirect to sign-in page
    return redirect('/sign-in')

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
            return redirect('/')
            
    return render(request, 'user/sign-in.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
        print(form)

    return render(request, 'user/sign-up.html', {'form': form})