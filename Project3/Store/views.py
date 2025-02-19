from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from datetime import datetime
from django.http import JsonResponse
from django.conf import settings
import hmac
import hashlib
import razorpay

# Create your views here.
def home(request):
    products=furnituredetails.objects.all()

    user=request.user
    if user.is_authenticated:
        usr=signup.objects.filter(user=user).first()
        wishlist_user=Wishlist.objects.filter(customer_id=usr)
        wishlist_item=wishlist_user.values_list('product_id', flat=True)
        # print(usr)
        context={
            'user':usr,
            'products':products,
            'wishlist_item':wishlist_item,
        }
        return render(request,'index.html',context)
    else:
        context={
            'user':None,
            'products':products
        }
        return render(request,'index.html',context)
    

def usersignup(request):
    if request.method=='POST':
        email=request.POST['email']
        createpassword=request.POST['createpassword']
        password=request.POST['confirmpassword']
        print(email,password,'newwwwwwwwwwwwwwwwwwww')
        if(createpassword!=password):
            print("The Password does not match")
            return redirect('store_app:loginpage')
        else:
            User.objects.create_user(username=email,password=password).save()
            usr=authenticate(username=email,password=password)
            signup.objects.create(user=usr,email=email,createpassword=createpassword,password=password)
            print("New user was created")
            return redirect('store_app:loginpage')
    
def userlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        print(email,password,'okkkkkkkkkkkkkkk')
        # login.objects.create(email=email,password=password)
        ur=authenticate(request,username=email,password=password)
        if ur is not None and hasattr(ur,'userdata'):
            login(request,ur)
            print("User Found")
            return redirect('store_app:home')
        elif ur is not None:
            login(request,ur)
            print("Admin login")
            return redirect('store_app:dashboard')
        else:
            print(ur,email,password,"No user was found")
            return redirect('store_app:loginpage')

# def usermessage(request):
#     if request.method=="POST";\:

#Admin Dashboard
def dashboard(request):
    return render(request,'dashboard.html')

#Enter store items

def storeitems(request):
    return render(request,'forms/storeitem.html')

def storedetail(request):
    if request.method=='POST':
        productid=request.POST['productid']
        productname=request.POST['productname']
        productimage=request.FILES['productimage']
        productprice=request.POST['productprice']
        productdesc=request.POST['productdesc']
        productmanu=request.POST['productmanu']
        productdime=request.POST['productdime']
        productstock=request.POST['productstock']
        product_pay=request.POST['product_pay']
        print(productid, productname, productimage, productprice)
        furnituredetails.objects.create(productid=productid, productname=productname, productimage=productimage, productprice=productprice,
                                        productdesc=productdesc, productmanu=productmanu, productdime=productdime,productstock=productstock,product_pay=product_pay)
        print('Sucessfully created')
        return redirect('store_app:storeitems')
    
#Edit Store items

def edititem(request):
    products=furnituredetails.objects.all()
    context={
            'products':products
        }
    return render(request,'forms/Itemedit.html',context)


def del_item(request,p_id):

    data=furnituredetails.objects.get(productid=p_id)
    data.delete()
    print(p_id, "was deleted")
    return redirect('store_app:itemedit')

def editupdate(request):
    if request.method=='POST':
        productid=request.POST['newproductid']
        newproductname=request.POST['newproductname']
        newproductimg=request.FILES.get('newproductimage')
        newproductprice=request.POST['newproductprice']
        newproductdesc=request.POST['newproductdesc']
        newproductmanu=request.POST['newproductmanu']
        newproductdime=request.POST['newproductdime']
        newproductstock=request.POST['newproductstock']
        product_pay=request.POST['product_pay']
        print(productid,newproductname,newproductimg,newproductprice,product_pay)
        my_product=furnituredetails.objects.get(productid=productid)
        my_product.productname=newproductname
        if newproductimg:
            my_product.productimage=newproductimg
        my_product.productprice=newproductprice
        my_product.productdesc=newproductdesc
        my_product.productmanu=newproductmanu
        my_product.productdime=newproductdime
        my_product.productstock=newproductstock
        my_product.product_pay=product_pay
        my_product.save()
        return redirect('store_app:itemedit')

#LOGOUT
def signout(request):
    logout(request)
    return redirect('store_app:home')

def furniture(request):
    user = request.user
    profile = signup.objects.get(user=user)
    products=furnituredetails.objects.all()
    wishlist_user=Wishlist.objects.filter(customer_id=profile)
    wishlist_item=wishlist_user.values_list('product_id', flat=True)
    context={
        'products':products,
        'wishlist_item':wishlist_item,
    }
    return render(request,'furniture.html',context)

def display(request,item):
    product=furnituredetails.objects.filter(id=item)
    context={
        'product':product
    }
    return render(request,'display.html',context)

def sales(request):
    sales=Purchase.objects.all()
    context={
            'sales':sales,
        }
    return render(request,'forms/sales.html',context)


def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def loginpage(request):
    return render(request,'loginpage.html')


def buy_product(request,p_id):
    usr=request.user
    current_user=signup.objects.get(user=usr)
    product_details=furnituredetails.objects.get(id=p_id)
    if request.method=='POST':
        quantity=int(request.POST['qty'])
        price=product_details.productprice
        totalprice=quantity*price
        print(totalprice, price, quantity, product_details.productprice)
        Purchase.objects.create(customers=current_user,product=product_details,qty=quantity,finalprice=totalprice)
        print("successfully placed order")
        return redirect('store_app:furniture')
    
def wish_list(request,p_id):
    usr=request.user
    current_user=signup.objects.get(user=usr)
    product=furnituredetails.objects.get(id=p_id)
    Wishlist.objects.create(customer_id=current_user, product_id=product)
    return JsonResponse({'message': 'Product added to wishlist!'})

def unlist_wish(request, p_id):
    print('okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    usr = request.user
    current_user = signup.objects.get(user=usr)
    product = furnituredetails.objects.get(id=p_id)
    Wishlist.objects.filter(customer_id=current_user, product_id=product).delete()
    return JsonResponse({'message': 'Product removed from wishlist!'})

def payment_page(request,item):
    product=furnituredetails.objects.filter(id=item)
    context={
        'product':product
    }
    return render(request,'Payment.html',context)

client=razorpay.Client(auth=(settings.KEY,settings.SECRET))


def plan_details(request,slug,item):
    if not request.user.is_authenticated:
        print("Login & Try Again")
        return redirect('store_app:loginpage')
    # plan = get_object_or_404(Plan, slug=slug)
    plan=furnituredetails.objects.filter(id=item)
    key = settings.KEY
    amount = plan.productprice * 100  # Amount in paise
    currency = 'INR'
    order = client.order.create({'amount': amount, 'currency': currency, 'payment_capture': "1"})        # RAZORPAY_KEY = settings.KEY
    print("Order ID:", order['id'])
    print(order)
    order_id = order['id']
    order_amount = order['amount']
    order_currency = order['currency']
    secret = settings.SECRET
    print(order_id, order_currency, order_amount, secret)
    return redirect('store_app:payment_page')