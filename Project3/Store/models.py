from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class contactus(models.Model):
    yourname=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()

class signup(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdata',blank=True,null=True)
    email=models.EmailField()
    createpassword=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    # user deatails
    fullname=models.CharField(max_length=50, default='NA')
    dateofbirth=models.DateField(null=True, blank=True)
    address=models.CharField(max_length=100, default='NA')
    state=models.CharField(max_length=30, default='NA')
    city=models.CharField(max_length=30, default='NA')
    postcode=models.IntegerField(default='000000')

    def __str__(self):
       return self.email
   

class login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=25)

class furnituredetails(models.Model):
    productid=models.IntegerField(unique=True)
    productname=models.CharField(max_length=50)
    productimage=models.ImageField(upload_to='productimages')
    productprice=models.IntegerField()
    productdesc=models.TextField(default='No description available')
    productmanu=models.CharField(max_length=50, default='NA')
    productdime=models.CharField(max_length=50, default='NA')
    productstock=models.BigIntegerField(default='0')
    product_pay=models.CharField(max_length=100, default='NA')

class Purchase(models.Model):
    customers=models.ForeignKey(signup,on_delete=models.CASCADE,blank=True,null=True)
    product=models.ForeignKey(furnituredetails,on_delete=models.CASCADE,blank=True,null=True)
    qty=models.IntegerField(default='0')
    finalprice=models.IntegerField(default='0')

class Wishlist(models.Model):
    customer_id=models.ForeignKey(signup, on_delete=models.CASCADE, blank=True,null=True)
    product_id=models.ForeignKey(furnituredetails, on_delete=models.CASCADE, blank=True, null=True)