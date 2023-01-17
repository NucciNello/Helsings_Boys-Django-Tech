from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
# from django.utils import timezone


class Profile(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)

   


    email = models.EmailField(_('email'), null=True, unique=True)
    reg_no = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(_('username'), max_length=30, blank=True, unique=True)
    password = models.CharField(max_length=10, blank = True, unique=False)
    first_name = models.CharField(_('firstname'), max_length=30, blank=True)
    last_name = models.CharField(_('lastname'), max_length=30, blank=True)
    second_name = models.CharField( max_length = 20, null = True, blank = True)
    dob = models.DateField(null = True,)
    mobile = models.CharField( max_length = 15, blank = True, null = True, unique = True)
    facebook = models.CharField( max_length = 20, null = True, blank = True)
    twitter = models.CharField( max_length = 20, null = True, blank = True)
    instagram = models.CharField( max_length = 20, null = True, blank = True)
    cv = models.FileField( null = False, blank = True, upload_to = None)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    
    is_admin = models.BooleanField(_('admin'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 

    def create_reg_no(self):
        return f"SO22-04-{self.id}"

    # @property
    # def sid(self):
    #     return "2022" % self.id

    class Meta:
        abstract = False
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **extra_fields):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **extra_fields) 

class Alumnus(models.Model):
    # name = models.CharField( max_length = 30, null = False, blank = False)
    name = models.CharField(max_length=10, null=False, blank=False)
    enrolled = models.CharField(max_length = 10, null = False, blank = False)
    graduated = models.CharField(max_length = 10, null = False, blank = False)
    headmaster = models.CharField(max_length = 15, null = False, blank = False)
    famous = models.CharField(max_length = 15, null = False, blank = False)
    results = models.CharField(max_length = 10, null = False, blank = False)
    occupation = models.CharField(max_length = 15, null = False, blank = False)
    email = models.CharField(max_length = 20, null = False, blank = False)
    address = models.CharField(max_length = 10, null = False, blank = False)
    mobile = models.CharField(max_length = 15, null = False, blank = False)

    class Meta:
        verbose_name = _('alumnus')
        verbose_name_plural = _('alumni')


    def __str__(self): 
        return self.name







# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

# class Registered(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE, default = False)

#     second_name = models.CharField( max_length = 20, null = False, blank = False)
#     dob = models.DateField(null = True,)
#     mobile = models.CharField( max_length = 15, null=False, blank = False, unique = True)
#     facebook = models.CharField( max_length = 20, null = True, blank = True)
#     twitter = models.CharField( max_length = 20, null = True, blank = True)
#     instagram = models.CharField( max_length = 20, null = True, blank = True)
#     cv = models.FileField( null = False, blank = False, upload_to = None)
#     date_created = models.DateTimeField(default = timezone.now)

#     def __str__(self): 
#         return self.user.first_name +' '+ self.user.last_name

#     class Meta:
#         verbose_name_plural = "Register"
        
