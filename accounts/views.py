from typing import ContextManager
from django.contrib import messages
from django.shortcuts import render, redirect
from . forms import SignUpForm, SingInForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User, auth

# Create your views here.

def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)    
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect("homepage")
    else:
        form = SignUpForm()

    context = {"form":form}
    return render(request,"accounts/sign-up.html",context )
