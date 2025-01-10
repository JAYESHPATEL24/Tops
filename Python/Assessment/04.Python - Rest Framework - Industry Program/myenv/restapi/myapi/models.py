from django.db import models

# Create your models here.

class User(models.Model): 
    postId = models.IntegerField(default=1) 
    name = models.CharField(max_length=100) 
    email = models.EmailField() 
    body = models.TextField(default="")

    def __str__(self):
        return self.name