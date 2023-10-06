from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *

def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    if request.method == "POST":
        data = contactUs()
        data.name = request.POST.get("name")
        data.email = request.POST.get("email")
        data.desc = request.POST.get("msg")
        data.created_date = datetime.now()
        data.save()
        messages.info(request,"Message send Successfully.")
        return redirect("/contact/")
    
    return render(request,"contact.html")


@login_required(login_url="/user_login/")
def dashboard(request):
    myuser = request.user
    data = to_do_data.objects.filter(user=myuser).order_by("-id")
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("description")
        data = to_do_data(title=title, desc=desc , user=myuser)
        data.save()
        return redirect('/dashboard/')
    return render(request,"dashboard.html",{"to_do_data":data})


def update(request,id):
        data = to_do_data.objects.get(id=id)
        if request.method == 'POST':
            data.title = request.POST.get("title")
            data.desc = request.POST.get("description")
            data.save()
            return redirect('/dashboard/')
        
        return render(request,"update.html",{"to_do_data":data})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            if (user.is_superuser):
                return redirect("/admin/")
            else:
                return redirect("/dashboard/")
        else:
            messages.error(request,"User Name or Password Incorrect, Try Again...")
    return render(request,"login.html")


def del_data(request,id):
    to_do_data.objects.get(id=id).delete()
    return redirect("/dashboard/")


def user_logout(request): 
    logout(request)
    return redirect("/")


def my_signup(request):
    if request.method == "POST":
        first_name = request.POST.get("name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        username = username.lower()
        if password!=cpassword:
            messages.info(request,"Passwords mismatch.")
            return redirect("/my_signup/")
        else:
            user = User.objects.filter(username=username)
            if user.exists():
                messages.info(request,"Username Already Taken.")
                return redirect("/my_signup/")
            user = User.objects.create(
                first_name = first_name,
                username = username
            )
            user.set_password(password)
            user.save()
            messages.info(request,"Account Created Successfully.")
            return redirect("/my_signup/")

    return render(request,"signup.html")

