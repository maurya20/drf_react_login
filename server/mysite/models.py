# Extending User Model 
# Using a Custom Model
# Extending AbstractUser


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# custom user model
class User(AbstractUser):
    
    username = models.CharField(max_length=55)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

 


#One to one related model for user profile 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = PhoneNumberField(blank=True, null=True)
    country = models.CharField(max_length=50,blank=True, null=True)
    city = models.CharField(max_length=50,blank=True, null=True)
    hobbies = models.CharField(max_length=150,blank=True, null=True)
   
    