"""
URL configuration for carbook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tokenize import Single
from django.contrib import admin
from django.urls import include,path
from.import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('signup/', views.signup, name='signup'),
    path('car/', views.car, name='car'),
    path('main/', views.main, name='main'),
    path('car_single/ <int:pk>', views.car_single, name='car_single'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cpass/', views.cpass, name='cpass'),
    path('fpass/', views.fpass, name='fpass'),
    path('otp/', views.otp, name='otp'),
    path('npass/', views.npass, name='npass'),
    path('uprofile/', views.uprofile, name='uprofile'),
    path('bindex/', views.bindex, name='bindex'),
    path('bpass/', views.bpass, name='bpass'),
    path('addcar/', views.addcar, name='addcar'),
    path('viewcar/', views.viewcar, name='viewcar'),
    path('editcar/ <int:pk>', views.editcar, name='editcar'),
    path('deletecar/ <int:pk>', views.deletecar, name='deletecar'),
    path('addcart/ <int:pk>', views.addcart, name='addcart'),
    path('cart/ ', views.cart, name='cart'),
    path('deletecart/ <int:pk>', views.deletecart, name='deletecart'),
    path('cart_car_single/ <int:pk>', views.cart_car_single, name='cart_car_single'),
    path('thankyou/ <int:pk>', views.thankyou, name='thankyou')
]
