from django.shortcuts import render,redirect
from . models import *
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    packagename=pkadmin.objects.all()
    context={
        'packagename':packagename
    }
    return render(request,'home.html',context)


def signup(request):    #User Registration
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(fname,lname,username,email,password)
        Register.objects.create(fname=fname,lname=lname,username=username,email=email,password=password)
        # Register(fname=fname,lname=lname,username=username,email=email,password=password).save()
        return redirect(regi)
    
def userlogin(request):   #User Login
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        if Register.objects.filter(username='Gadmin',password='12345').exists():
            return redirect(packadmin)
        else:
            if Register.objects.filter(username=username,password=password).exists():
                return redirect(pack)
            else:
                return redirect(regi)

    
def learndb(request):       #Just to learn DB not in use
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        print(fname,lname,email,password,'sucess')
        NewReg.objects.create(fname=fname,lname=lname,email=email,password=password)
        return redirect(regi2)
    
def packcreate(request):        #Package Creation
    if request.method == 'POST':
        packname=request.POST['packname']
        packprice=request.POST['packprice']
        packdesc=request.POST['packdesc']
        packimg=request.FILES['packimg']
        

        cancel=request.POST['cancel']
        if cancel:
            cancel=True
        else:
            cancel=False
        duration=request.POST['duration']
        guide=request.POST['guide']
        groupsize=request.POST['groupsize']
        #print(packname,packprice,packdesc,packimg,cancel,duration,guide,groupsize)
        pkadmin.objects.create(packname=packname,packprice=packprice,packdesc=packdesc,packimg=packimg,
                               cancel=cancel,duration=duration,guide=guide,groupsize=groupsize)
        return redirect(packadmin)
    
#change password
def changepass(request):
    return render(request,'Regi/updatepass.html')

def newpass(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        newpassword=request.POST['newpassword']
        print(username,password,newpassword)
        if Register.objects.filter(username=username,password=password).exists():
            print('username exists')
            user=Register.objects.get(username=username,password=password)
            user.username=newpassword
            user.save()
            return redirect(regi)

        else:  
            print('username does not exists')
        return redirect(changepass)
    
#Forgot Password
def forgot(request):
    return render(request,'Regi/forgotpass.html')

def fpass(request):
    username=request.POST['username']
    email=request.POST['email']
    if Register.objects.filter(username=username,email=email).exists():
        print(username,email)
        request.session['email']=email

        message=random.randint(10000,99999)  #OTP generation
        my_otp=f'your verification code:{message}'

        send_mail('Otpcode',my_otp,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        request.session['message']=message
        return redirect(otp)
    else:
        print('NO MATCH FOUND')
        return redirect(forgot)
    
def getotp(request):            #OTP page confirmation
    inotp=request.POST['inotp']
    message=request.session['message']

    if(int(inotp)==message):
        print('RightOTP')
        return redirect(newpassconfirm)
    else:
        print('Wrong OTP')
        print(inotp)
        print(message)
        return redirect(otp)
    
def newpassword(request):           #New password after reset
    cpass=request.POST['cpass']
    npass=request.POST['npass']
    if(npass!=cpass):
        msg='password not mstch'
        context={
            'msg':msg
        }
        return render(request,'Regi/newpassconfirm.html',context)
    
    else:
        email=request.session['email']
        Register.objects.filter(email=email).update(password=cpass)
        print('Updated')
        return redirect(regi)
     

def otp(request):
    return render(request,'Regi/otp.html')

def newpassconfirm(request):
    return render(request,'Regi/newpassconfirm.html')
    
#webpages
def pack(request):
    return render(request,'other/package.html')
    
def packadmin(request):
    return render(request,'other/packadmin.html')

def regi2(request):
    return render(request,'Regi/regi2.html')

def dest(request):
    return render(request,'page/destination.html')

def chugoku(request):
    return render(request,'page/chugoku.html')

def hokkaido(request):
    return render(request,'page/hokkaido.html')

def hokuriku(request):
    return render(request,'page/hokuriku.html')

def kansai(request):
    return render(request,'page/kansai.html')

def kanto(request):
    return render(request,'page/kanto.html')

def kyushu(request):
    return render(request,'page/kyushu.html')

def okinawa(request):
    return render(request,'page/okinawa.html')

def sample(request):
    return render(request,'page/Sample.html')

def shikoku(request):
    return render(request,'page/shikoku.html')

def tohoku(request):
    return render(request,'page/tohoku.html')

def tokai(request):
    return render(request,'page/tokai.html')

def error(request):
    return render(request,'other/error.html')

def news(request):
    return render(request,'news.html')

def pyt(request):
    return render(request,'other/pyt.html')

def ttd(request):
    return render(request,'other/ttd.html')

def regi(request):
    return render(request,'Regi/regi.html')