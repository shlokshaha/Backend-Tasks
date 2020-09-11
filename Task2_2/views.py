from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import Profile


def signup(request):
    if request.method=='POST':
        info = request.POST
        if info['password1'] == info['password2']:
            username = info['username']
            password = info['password1']
            email = info['email']
            fname = info['fname']
            lname = info['lname']
            phno = info['phno']
            try:
                user=User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname)
                profile=Profile(user=user, phone_number=phno)
                profile.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('login')
            except:
                return render(request, 'Task2_2/signup.html',{"msg":'User With The Given Username Already Exists !'})
        return render(request, 'Task2_2/signup.html',{'error':"Passwords Don't Match"})
    return render(request, 'Task2_2/signup.html')


def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('success')
        return render(request,"Task2_2/login.html",{'error':"Invalid Credentials!"})
    return render(request,'Task2_2/login.html')


def success(request):
    return render(request,'Task2_2/success.html')


def logout_user(request):
    logout(request)
    return render(request,"Task2_2/signup.html",{'logoutmsg':"Logged Out Successfully \n Log In/SignUp Again!"})