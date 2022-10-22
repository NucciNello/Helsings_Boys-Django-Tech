from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Registered(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = False)

    second_name = models.CharField( max_length = 20, null = False, blank = False)
    dob = models.DateField(null = True,)
    mobile = models.CharField( max_length = 15, null=False, blank = False, unique = True)
    facebook = models.CharField( max_length = 20, null = True, blank = True)
    twitter = models.CharField( max_length = 20, null = True, blank = True)
    instagram = models.CharField( max_length = 20, null = True, blank = True)
    cv = models.FileField( null = False, blank = False, upload_to = None)
    date_created = models.DateTimeField(default = timezone.now)

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
