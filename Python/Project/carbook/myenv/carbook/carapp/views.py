from django.shortcuts import render,redirect
from . models import *
import random, requests
from django.conf import settings
# from django.http import JsonResponse,HttpResponse
from django.views.decorators.cache import never_cache
# import json
import razorpay

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def signup(request):
    
    if request.method == "POST" :
        try:
            user = User.objects.get(email=request.POST['email'])
            msg = "Already Register!!"
            return render(request, 'signup.html', {'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    email = request.POST['email'],
                    name = request.POST['name'],
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    profile = request.FILES['profile'],
                    usertype = request.POST['Usertype']
                )
                msg = "Sign Up Successfully..!!!"
                return render(request, 'login.html', {'s_msg':msg})
            else:
                msg = "Invalid Credintials..!!!"
                return render(request, 'signup.html', {'msg':msg})
        
    else:
        return render(request, 'signup.html')

def car(request):
    user = User.objects.get(email=request.session['email'])
    cars = Car.objects.all()
    return render(request, 'car.html', {'cars':cars})

def main(request):
    return render(request, 'main.html')

def car_single(request,pk):
    user = User.objects.get(email=request.session['email'])
    car = Car.objects.get(pk=pk)
    return render(request, 'car_single.html', {'car':car})

@never_cache
def login(request):
    if request.session.get('email'):
        user = User.objects.get(email=request.session['email'])
        if user.usertype == "customer":
            return redirect('index')
        else:
            return redirect('bindex')
        
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['profile'] = user.profile.url
                if user.usertype=="customer":
                    return redirect('index')
                else:
                    return redirect('bindex')
            else:
                msg = "invalid password....!!!!"
                return render(request,'login.html', {'msg':msg})
        except:
            msg = "Email isn't registered...!!!"
            return render(request,'login.html', {'msg':msg})

    else:
        return render(request, 'login.html')
    
def cpass(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        try:
            if user.password==request.POST['opassword']:
                if request.POST['npassword'] == request.POST['cnpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect('logout')
                else:
                    msg = "New password & new Confirm Password Doesn't match...!!!"
                    if user.usertype=="customer":
                        return render(request, 'cpass.html',{'msg':msg})
                    else:
                        return render(request, 'bpass.html', {'msg':msg})
            else:
                msg = "Old Password Doesn't match...!!!!"
                if user.usertype=="customer":
                    return render(request, 'cpass.html',{'msg':msg})
                else:
                    return render(request, 'bpass.html', {'msg':msg})
        except:
            pass
    else:
        if user.usertype=="customer":
            return render(request, 'cpass.html')
        else:
            return render(request, 'bpass.html')
    
def fpass(request):
    if request.method == "POST":
        try:
            user = User.objects.get(mobile=request.POST['mobile'])
            mobile = request.POST['mobile']
            otp = random.randint(1001,9999)

            print(f"otp : {otp}")

            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"8evG5QY4crJE3sZp9bayOMzRNunlILofWDTVwAqjkBthSxXCP69mb76cB5UNVWlrifAZHRkygJ0qwhCa","variables_values":otp,"route":"otp","numbers":mobile}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            request.session['mobile'] = user.mobile
            request.session['otp'] = otp
            return render(request,'otp.html')
        except:
            msg = "Mobile number is not register!!!!"
            print("Hello")
            return render(request, 'fpass.html', {'msg': msg})
    else:
        return render(request, "fpass.html")
    
def otp(request):
    otp = int(request.session['otp'])
    uotp = int(request.POST['uotp'])
    try:
        if otp == uotp:
            del request.session['otp']
            return render(request, 'npass.html')
        else:
            msg = "Invalid Otp!!!"
            return render(request,'otp.html',{'msg':msg})
    except:
        return render(request, 'otp.html')

def npass(request):
    user = User.objects.get(mobile = request.session['mobile'])
    if request.method=="POST":
        try:
            if request.POST['npassword'] == request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                del request.session['mobile']
                return redirect('login')
            else:
                msg = "New Password & new confirm Password doesn't match...!!!"
                return render(request,'npass.html',{'msg':msg})
        except:
            pass
    else:
        return render(request, 'npass.html')

def uprofile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.name=request.POST['name']
        user.mobile=request.POST['mobile']
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['profile']=user.profile.url
        except:
            pass
        user.save()
        if user.usertype=="customer":
            return redirect('index')
        else:
            return redirect('bindex')
    else:
        return render(request, 'uprofile.html',{'user':user})

def logout(request):
    del request.session['email']
    del request.session['profile']
    return redirect('login')

def bindex(request):
    return render(request, 'bindex.html')

def bpass(request):
    return render(request, 'bpass.html')

def addcar(request):
    if request.method == "POST" :
        try:
            user = User.objects.get(email=request.session['email'])
            Car.objects.create(
                user=user,
                stransmission = request.POST['stransmission'],
                sfuel = request.POST['sfuel'],
                cname = request.POST['cname'],
                cyear = request.POST['cyear'],
                cprice = request.POST['cprice'],
                mileage = request.POST['mileage'],
                desc = request.POST['desc'],
                cimage = request.FILES['cimage']
            )

            msg = "Car Added Successfully....!!!"
            return render(request, 'addcar.html', {'msg':msg})

        except Exception as e:
            print(e)
            return render(request, 'addcar.html')
    
    else:
        return render(request, 'addcar.html')

def viewcar(request):
    user = User.objects.get(email=request.session['email'])
    cars = Car.objects.filter(user=user)
    return render(request, 'viewcar.html', {'cars':cars})

def editcar(request,pk):
    user = User.objects.get(email=request.session['email'])
    car = Car.objects.get(pk=pk)

    if request.method == "POST":
        car.stransmission = request.POST['stransmission']
        car.sfuel = request.POST['sfuel']
        car.cname = request.POST['cname']
        car.cyear = request.POST['cyear']
        car.cprice = request.POST['cprice']
        car.mileage = request.POST['mileage'] 
        car.desc = request.POST['desc']   

        try:
            car.cimage = request.FILES['cimage']
            car.save()
        except:
            pass

        car.save()

        return redirect('viewcar')

    else:
        return render(request, 'editcar.html', {'car':car})

def deletecar(request,pk):
    user = User.objects.get(email=request.session['email'])
    car = Car.objects.get(pk=pk)

    if request.method == "POST":

        car.delete()
        return redirect('viewcar')
    
    else:
        return render(request, 'deletecar.html')
    
def addcart(request, pk):
    user = User.objects.get(email=request.session['email'])
    car = Car.objects.get(pk=pk)
    cart = Cart.objects.filter(user=user,car=car)
    if cart:
        msg = "Car is already added in Cart."
        cars = Car.objects.all()
        return render(request, "car.html",{'msg':msg, 'cars':cars, 'carpk':pk})
    else:
        Cart.objects.create(
            user=user,
            car=car
        )

        return redirect('car')
    
def cart(request):
    user = User.objects.get(email=request.session['email'])
    cart = Cart.objects.filter(user=user, payment=False)

    net = 0
    for i in cart:
        net += i.car.cprice

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    try:
        payment = client.order.create({'amount': net * 100, 'currency': 'INR', 'payment_capture': 1})
    except Exception as e:
        print("Razorpay Error:", e)  # Debugging line
        return redirect('car')

    context = {
        'payment': payment,
    }

    return render(request, 'cart.html', {'cart': cart, 'net': net, 'context': context})



def cart_car_single(request, pk): 
    user = User.objects.get(email=request.session['email']) 
    cart_items = Cart.objects.filter(user=user, pk=pk)  
    cart = cart_items.first() 
    car = cart.car 
    return render(request, "car_single.html", {"car": car})


def deletecart(request,pk):
    user = User.objects.get(email=request.session['email'])
    cart = Cart.objects.filter(pk=pk)

    cart.delete()

    return redirect('cart')

def thankyou(request):
    try:
        user = User.objects.get(email=request.session['email'])
        cart = Cart.objects.filter(user=user)

        cart.payment = True

        return render(request,'thankyou.html')

    except:
        return redirect('index')
