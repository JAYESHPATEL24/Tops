from rest_framework import serializers 
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['postId', 'id', 'name', 'email', 'body']
        # fields = '__all__'
