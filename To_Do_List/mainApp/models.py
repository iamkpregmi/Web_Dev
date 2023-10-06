from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class myUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True )

class to_do_data(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True )

class contactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField()
    created_date = models.DateTimeField(default=datetime.now())

