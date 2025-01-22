
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 
from .models import UserTypes


class CustomUserManager(BaseUserManager):

    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valide email address"))
        
    def create_user(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError(_('User must provide an email address'))
        if not password:
            raise ValueError('User must provide a password')
        
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None,**extra_fields):
        
        if not email:
            raise ValueError('Base User Account: Super users must provide an email address')
        if not password:
            raise ValueError('Base User Account: Super users must provide a password')
        
        user = self.create_user(email=email, password=password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        user.save()
        return user