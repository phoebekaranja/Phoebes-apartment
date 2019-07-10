from django.db import models
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class House(models.Model):
    house_image=models.ImageField(upload_to='businesses',null=True)
    house_number=models.CharField(max_length =10)
    tenant=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    status=models.CharField(max_length =10)

    def __str__(self):
        return self.house_number
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profiles',null=True)
    user_name=models.OneToOneField(User,null=True,on_delete=models.CASCADE,related_name="user")
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length = 10,blank = True)


    def __str__(self):
        return self.user_name

    def save_profile():
        self.save()        