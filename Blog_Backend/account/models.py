from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db.models.signals import post_save
from django.dispatch import receiver

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

def profile_pic_uploaded(instance,filename):
    return 'uploads\{user}\{filename}'.format(user=instance.user.username,filename=filename)

class AccountDetail(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE,related_name='account')
    bio = models.CharField(max_length=100, null=True, blank=True)
    fullname = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(upload_to=profile_pic_uploaded, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Account)
def create_account_detail(sender, instance, created, **kwargs):
    if created:
        AccountDetail.objects.create(user = instance)

@receiver(post_save, sender=Account)
def save_account_detail(sender, instance, **kwargs):
    instance.account.save()