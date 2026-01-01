from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request, 
            username=username, 
            password=password
        )

        if user is not None:
            # Log user in
            login(request, user)
            return redirect('/')
            
    return render(request, 'user/sign-in.html')