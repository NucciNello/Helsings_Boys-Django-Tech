# from email.policy import default
# from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Registered

# Create your models here.
# class Reg_users(AbstractBaseUser, PermissionsMixin):


class Registered(models.Model):
# class Registered(AbstractUser):

    user = models.ForeignKey(User, on_delete = models.CASCADE, default = False)

    # email = models.EmailField( max_length = 50)
    # first_name = models.CharField( max_length = 20, blank = False, null = False)
    # last_name = models.CharField( max_length = 20, null = False, blank = False)
    # username = models.CharField( max_length = 20, null = False, blank = False, unique = True)
    # password = models.CharField( max_length=10, null = False, blank = False)

    second_name = models.CharField( max_length = 20, null = False, blank = False)
    dob = models.DateField(null = True,)
    mobile = models.CharField( max_length = 15, null=False, blank = False, unique = True)
    facebook = models.CharField( max_length = 20, null = True, blank = True)
    twitter = models.CharField( max_length = 20, null = True, blank = True)
    instagram = models.CharField( max_length = 20, null = True, blank = True)
    cv = models.FileField( null = False, blank = False, upload_to = None)
    date_created = models.DateTimeField(default = timezone.now)

    # REQUIRED_FIELDS = ['password', 'is_staff']
    # USERNAME_FIELD = 'username'

    def __str__(self): 
        return self.user.first_name +' '+ self.user.last_name


class Alumnus(models.Model):
    name = models.CharField( max_length = 30, null = False, blank = False)
    enrolled = models.CharField(max_length = 10, null = False, blank = False)
    graduated = models.CharField(max_length = 10, null = False, blank = False)
    headmaster = models.CharField(max_length = 15, null = False, blank = False)
    famous = models.CharField(max_length = 15, null = False, blank = False)
    results = models.CharField(max_length = 10, null = False, blank = False)
    occupation = models.CharField(max_length = 15, null = False, blank = False)
    email = models.CharField(max_length = 20, null = False, blank = False)
    address = models.CharField(max_length = 10, null = False, blank = False)
    mobile = models.CharField(max_length = 15, null = False, blank = False)

    def __str__(self): 
        return self.name

















# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#      if created:
#         Registered.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.registered.save()

    # is_active = models.BooleanField(default = False)
    # is_superuser = models.BooleanField(default = False)
    # is_anonymous = models.BooleanField(default = False)
    # is_authenticated = models.BooleanField(default = False)
    # is_staff = models.BooleanField(default = False)