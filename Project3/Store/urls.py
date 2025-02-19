from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='store_app'

urlpatterns = [
    path('', views.home,name='home'),

    # signup
    path('signup', views.usersignup, name='signup'),

    #login
    path('login', views.userlogin, name='login'),

    path('furniture/', views.furniture, name='furniture',),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('loginpage/', views.loginpage,name='loginpage'),
    path('signout',views.signout,name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.storeitems, name='products'),
    path('storedetails', views.storedetail, name='storedetails'),
    path('itemedit/', views.edititem, name='itemedit'),
    path('edit', views.editupdate, name='edit'),
    path('del_item/<int:p_id>/',views.del_item,name='del_item'),
    path('display/<int:item>/', views.display, name='display'),
    path('buy_product/<int:p_id>/', views.buy_product, name='buy_product'),
    path('sales/', views.sales, name='sales'),
    path('wish_list/<int:p_id>/', views.wish_list, name='wish_list'),
    path('unlist_wish/<int:p_id>/', views.unlist_wish, name='unlist_wish'),
    path('payment_page/<int:item>/', views.payment_page, name='payment_page'),
    path('plan_details/<int:item>/', views.plan_details, name='plan_details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
