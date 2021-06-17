from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user(request):
    return render(request, 'authenticate/user.html', {})


def SignUp(request):
    return render(request, 'authenticate/SignUp.html', {})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('Home');
        else:
            return redirect()
    else:
        return render(request, 'authenticate/Login.html', {})



