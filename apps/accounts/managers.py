
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 



class CustomUserManager(BaseUserManager):

    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valide email address"))
        
    def create_user(self, email,first_name,last_name,password=None,**extra_fields):
        if not email:
            raise ValueError(_('User must provide an email address'))
        if not password:
            raise ValueError('User must provide a password')
        if not first_name:
            raise ValueError('User must provide a first_name')
        if not last_name:
            raise ValueError('User must provide a last_name')
        
        user = self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,first_name,last_name, password=None,**extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if not email:
            raise ValueError('Base User Account: Super users must provide an email address')
        if not password:
            raise ValueError('Base User Account: Super users must provide a password')
        
        user = self.create_user(email=email,first_name=first_name,last_name=last_name, password=password,**extra_fields )
       

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")
        user.save()

        return user