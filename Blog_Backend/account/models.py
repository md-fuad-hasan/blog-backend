from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must need email')
        if not username:
            raise ValueError('User must need Username')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username)
        
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,username, password):
        email= self.normalize_email(email)
        user = self.create_user(email=email,username=username,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using = self._db) 

        return user


class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email
