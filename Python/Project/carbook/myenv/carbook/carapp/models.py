from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=20)
    profile = models.ImageField(default="", upload_to='profile/')
    usertype = models.CharField(max_length=20, default="customer")

    def __str__(self):
        return self.name
    

class Car(models.Model):

    transmission = (
        ('Auto','Auto'),
        ('Manual','Manual')
    )

    fuel = (
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('EV','EV')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stransmission = models.CharField(max_length=10, choices=transmission)
    sfuel = models.CharField(max_length=10, choices=fuel)
    cname = models.CharField(max_length=20)
    cyear = models.IntegerField()
    cprice = models.IntegerField()
    mileage = models.IntegerField() 
    desc = models.TextField()   
    cimage = models.ImageField(default="",upload_to="car_images/")

    def __str__(self):
        return self.cname

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    payment = models.BooleanField(default=False)
    ttime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.user.name} - {self.car} - {'Paid' if self.payment else 'Pending'}"
