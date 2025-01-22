from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManager



class User(AbstractBaseUser,PermissionsMixin):

    pkid = models.BigAutoField(primary_key=True,editable=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    email = models.EmailField(verbose_name=_("Email Address"),unique=True,db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
   
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("Customer Account")
        verbose_name_plural = _("Customer Accounts")
        ordering=["-created_at"]

    def __str__(self):
        return f"Customer account for {self.email}"



    
