from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            print(f"User {user.username} logged in")  
            return redirect("home")
        else:
            return HttpResponse("Ошибка авторизации")
    return render(request, "your_app/login.html")

def user_logout(request):
    print(f"User {request.user.username} logged out")  
    logout(request)
    return redirect("login")
