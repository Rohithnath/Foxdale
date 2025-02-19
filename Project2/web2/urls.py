from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from.import views
urlpatterns = [
    #Homepage
    path('', views.home, name='home'),

    #Userregistartion
    path('signup',views.signup,name='signup'), 

    #Userlogin
    path('userlogin',views.userlogin,name='userlogin'),

    #User change password
    path('changepass/',views.changepass,name='changepass'),
    path('newpass',views.newpass,name='newpass'),   #change password DB

    #Forgot Password
    path('forgotpass/',views.forgot,name='forgotpass'),
    path('fpass',views.fpass,name='fpass'),         #forgot password DB

    path('otp/',views.otp,name='otp'),              #OTP page
    path('otp',views.getotp,name='otp'),            #OTP DB
    path('resetpass',views.newpassword,name='resetpass'),

    path('newpasscon/',views.newpassconfirm,name='newpasscon'),

    #Package
    path('packcreate', views.packcreate, name='packcreate'), #Package Creation DB
    path('packadmin/', views.packadmin, name='packadmin'),   #Package Admin Page
    path('package/', views.pack, name='package'),            #Package User Page

    #Pages
    path('regi2/', views.regi2, name='regi2'),
    path('dest/', views.dest, name='dest'),
    path('chugoku', views.chugoku, name='chugoku'),
    path('hokkaido/', views.hokkaido, name='hokkaido'),
    path('hokuriku/', views.hokuriku, name='hokuriku'),
    path('kansai/', views.kansai, name='kansai'),
    path('kanto/', views.kanto, name='kanto'),
    path('kyushu/', views.kyushu, name='kyushu'),
    path('okinawa/', views.okinawa, name='okinawa'),
    path('sample/', views.sample, name='sample'),
    path('shikoku/', views.shikoku, name='shikoku'),
    path('tohoku', views.tohoku, name='tohoku'),
    path('tokai/', views.tokai, name='tokai'),
    path('error/', views.error, name='error'),
    path('news/', views.news, name='news'),
    path('pyt/', views.pyt, name='pyt'),
    path('ttd/', views.ttd, name='ttd'),
    path('regi/', views.regi, name='regi'),

    #sample
    path('learndb', views.learndb, name='learndb'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)