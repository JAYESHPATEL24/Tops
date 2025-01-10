from django.shortcuts import render
from rest_framework import generics 
from .models import User
from .serializers import UserSerializer

# Create your views here.
# user deatils list
class Userlist(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# change in user details (update, delete)
class Userdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer