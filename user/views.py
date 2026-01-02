from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout,get_user_model
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .form import RegisterForm



@login_required
def index(request):
    current_user = request.user
    return render(request, 'user/index.html',{'user': current_user})

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
        else:
            print("not successful")
            messages.info(request, "Sign in not successful. Please check your username and password")
            
    return render(request, 'user/sign-in.html')

def sign_up(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        print(username)
        print(email)
        print(password)
        print(confirm)
        if (password == confirm):
            user = User.objects.create_user(username = username, email= email, password= password)
            user.save()
            login(request, user)
            return redirect('/user/')
        else:
            messages.info(request, "Sign up not successful. Please check your password and confirm password")

    return render(request, 'user/sign-up.html')

# get
def get_users_as_json(request):
    col = ["username", "email","password"]
    User = get_user_model()
    all_users = User.objects.all().values(*col)
    user_list = list(all_users)
    return JsonResponse(user_list, safe=False)

#get specific
def get_one_user(request,username):
    User = get_user_model()
    user = User.objects.filter(username=username).values("username", "email","password").first()
    if user is not None:
        return JsonResponse(user, safe=False)
    else:
        return HttpResponse("Username not found")

# post
@csrf_exempt
def add_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username = username, email= email, password= password)
    user.save()
    return HttpResponse("request successful")
    
# update
@csrf_exempt
def password_change(request):
    username = request.POST.get('username')
    user = User.objects.filter(username = username).first()
    if user is None:
        return HttpResponse("Username not found")
    password = request.POST.get('password')
    user.set_password(password)
    user.save()
    return HttpResponse("request successful")

# delete
@csrf_exempt
def delete_user(request):
    username = request.POST.get('username')
    user = User.objects.filter(username = username).first()
    if user is None:
        return HttpResponse("Username not found")
    user.delete()
    return HttpResponse("request successful")

