from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from datetime import datetime
from Store.models import *
# Create your views here.

def userprofile(request):
    user = request.user
    profile = signup.objects.get(user=user)
    wishlist_cart=Wishlist.objects.filter(customer_id=profile)
    context = {  
        'profile': profile,
        'wishlist':wishlist_cart,
    }

    if request.method == 'POST':
        fullname = request.POST['fullname']
        date_input = request.POST['dateofbirth']
        date_input = request.POST['dateofbirth']
        date_formats = [
            "%B %d, %Y", "%b. %d, %Y", "%b %d, %Y", 
            "%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y",
            "%m-%d-%Y", "%m/%d/%Y", "%m.%d.%Y",
            "%Y-%m-%d", "%Y/%m/%d", "%Y.%m.%d",
            "%b. %d, %y", "%d-%m-%y", "%d/%m/%y",
            "%m-%d-%y", "%m/%d/%y"
        ]
        date_object = None
        dateofbirth = None

        if date_input:
            for date_format in date_formats:
                try:
                    date_object = datetime.strptime(date_input, date_format)
                    dateofbirth = date_object.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue


        address = request.POST.get('address', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        postcode = request.POST.get('postcode', '')

        profileupdate = signup.objects.get(user=user)
        profileupdate.fullname = fullname
        profileupdate.dateofbirth = dateofbirth
        profileupdate.address = address
        profileupdate.state = state
        profileupdate.city = city
        profileupdate.postcode = postcode
        profileupdate.save()
        return redirect('user_app:userprofile')

    return render(request, 'userprofile.html', context)


