from django.shortcuts import render,redirect
from .models import UserDetails

def home(request):
    if request.method == 'POST':
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        ph_no=request.POST['phno']
        email=request.POST['email']
        gender=request.POST['gender']

        profile=UserDetails(fname=f_name,lname=l_name,phno=ph_no,email=email,gender=gender)
        profile.save()
        return redirect('page2')

    return render(request,'Task2_1/home.html')

def page2(request):
    if request.method=='POST':
        email=request.POST['email']
        user=UserDetails.objects.filter(email=email)
        if not user:
            return render(request,'Task2_1/conclusion.html',{'msg':'Sorry No User With Entered Email Id Found'})
        return render(request,'Task2_1/conclusion.html',{'msg':'User Found!','data':user})
    return render(request,'Task2_1/page2.html')
