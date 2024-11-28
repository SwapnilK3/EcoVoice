from django.contrib.auth.models import AbstractBaseUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User as AuthUser
from .manager import CustomUserManager


class CustomUser(models.Model):
     
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True, blank=True)
   
    # Additional fields for complaint filing
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True)
    country = models.CharField(max_length=20, blank=True)
    
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
  
    # objects=CustomUserManager()   
    # USERNAME_FIELD ='email'
    # REQUIRED_FIELDS =['email']
    # groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    # user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


class Complaint(models.Model):
    
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True, blank=True)  
    crime_type = models.CharField(max_length=100, blank=True)
    is_anonymous = models.BooleanField()
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    crime_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)

    