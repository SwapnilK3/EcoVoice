from django.contrib.auth.models import AbstractBaseUser, Group , Permission
from django.db import models

from django.contrib.auth.models import User as AuthUser
from .manager import CustomUserManager


class CustomCharityUser(models.Model):
    
    
    
    # Additional fields for complaint filing
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
    charity_name = models.CharField(max_length=255, blank=True ,null=True)
    charity_id = models.CharField(max_length=15, unique=True, blank=True, null=True)
    charity_address = models.TextField(max_length=100, blank=True, null=True)
    charity_city = models.CharField(max_length=20, blank=True, null=True)
    charity_country = models.CharField(max_length=20, blank=True, null=True)
    charity_state = models.CharField(max_length=20, blank=True, null=True)
    charity_zipcode = models.CharField(max_length=10, blank=True, null=True)
    
    # objects=CustomUserManager()
    
    # USERNAME_FIELD ='email'
    # REQUIRED_FIELDS =['']
    # groups = models.ManyToManyField(Group, related_name='charity_user_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='charity_user_permissions')

class Profile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    email_token= models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    

class Event(models.Model):
    event_headline = models.CharField(max_length=100)
    event_address = models.CharField(max_length=100)
    event_city = models.CharField(max_length=100)
    event_state = models.CharField(max_length=100)
    event_country = models.CharField(max_length=100)
    #   event_type = models.CharField(max_length=100)
    event_host = models.CharField(max_length=100)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    event_zipcode = models.CharField(max_length=10, blank=True, null=True)
    
    
class Blog(models.Model):
    
    author_name = models.CharField(max_length=100)
    # + blog_type : text
    blog_heading = models.CharField(max_length=100)
    blog_description = models.TextField()
    uploaded_date = models.DateField(auto_now=False, auto_now_add=False)
    
class Donation(models.Model):
    donation_id =  models.CharField(max_length=100)
    donaor =  models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    trancaction_method= models.CharField(max_length=100)


#manager
