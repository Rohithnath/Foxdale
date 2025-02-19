from django.db import models

# Create your models here.


class Register(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class pkadmin(models.Model):       #PACKAGE DB for admin entry
    packname=models.CharField(max_length=50)
    packprice=models.CharField(max_length=50)
    packdesc=models.TextField()
    packimg=models.ImageField(upload_to='pics')
    cancel=models.BooleanField(default=False)
    duration=models.CharField(max_length=50)
    guide=models.CharField(max_length=50)
    groupsize=models.IntegerField()


class NewReg(models.Model):         #JuST SAMPLE DB
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)

class updatepass(models.Model):     #Change Password
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    newpassword=models.CharField(max_length=50)

class forgotpass(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()

class inotp(models.Model):
    otpdb=models.IntegerField()

class newpass(models.Model):
    cpass=models.CharField(max_length=50)