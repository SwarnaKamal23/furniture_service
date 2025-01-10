from django.shortcuts import render
from .models import Orders
from .models import Contact
import datetime as dt

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    if request.method=='POST':
        userName=request.POST['uname']
        userEmail=request.POST['uemail']
        userSubject=request.POST['usubject']
        userMessage=request.POST['umessage']

        print(userName,userEmail,userSubject,userMessage)

        row=Contact.objects.create(Name=userName,Email=userEmail,Subject=userSubject,Message=userMessage)
        row.save()
        return render(request,'contact.html')
    
    else:
        return render(request,'contact.html')

    return render(request,'contact.html')


def projects(request):
    return render(request,'project.html')

def features(request):
    return render(request,'feature.html')

def services(request):
    return render(request,'service.html')

def quotes(request):
    # if request.method=='POST':
    #     username=request.POST['uname']
    #     useremail=request.POST['umail']
    #     usercontact=request.POST['mobile']
    #     userservice=request.POST['service']
    #     # userbudget=request.POST['budget']
    #     usernote=request.POST['note']

    #     print(username,useremail,usercontact,userservice,usernote)

    #     row=Orders.objects.create(name=username,email=useremail,mobile=usercontact,service=userservice,note=usernote)
    #     row.save()

    
    #     return render(request,'index.html')
    # else:
    #     return render(request,'quote.html')

    return render(request,'quote.html')

@login_required(login_url='login')
def booking(request):
        if request.method=='POST':
            usercontact=request.POST['mobile']
            userservice=request.POST['service']
            username=request.POST['uname']
            useremail=request.POST['umail']
            usernote=request.POST['note']


            bid=username[0:4]+'-wood-2025'
            date=dt.datetime.now()
            bdate=date.strftime('%d-%m-%y & %H:%M:%S')
            cname=username
            ccontact=usercontact
            cservice=userservice
            cnote=usernote
            pickup_date=date+dt.timedelta(days=7)
            pdate=pickup_date.strftime('%d-%m-%y')
            date=pickup_date+dt.timedelta(days=15)
            ddate=date.strftime('%d-%m-%y')

            data={'bid':bid,'bdate':bdate,'cname':cname,'cnumber':ccontact,'staken':cservice,'snote':cnote,'pdate':pdate,'ddate':ddate}

            row=Orders.objects.create(name=username,email=useremail,mobile=usercontact,service=userservice,note=usernote)
            row.save()

        else:
            return render(request,'index.html')

        return render(request,'booking_info.html',data)


def teams(request):
    return render(request,'team.html')

def error(request):
    return render(request,'404.html')

def testimonials(request):
    return render(request,'testimonial.html')

def login_view(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['uname'],password=request.POST['upassword'])
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')

    return render(request,'login.html')

def sign_up(request):
    if request.method=='POST':
        name=request.POST['uname']
        usermail=request.POST['uemail']
        password=request.POST['upassword']
        cpassword=request.POST['uconpass']

        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,'account exists')
                return render(request,'sign_up.html')
            else:
                user=User.objects.create_user(username=name,password=password)
                login(request,user)
                messages.info(request,'account created successfully')
                return redirect('home')
        else:
            messages.error(request,'passwords dont match')


    return render(request,'sign_up.html')


@login_required
def logout_view(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('home')
