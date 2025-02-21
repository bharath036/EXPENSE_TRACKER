from django.db import models
from django.contrib.auth.models import AbstractUser 
from accounts.manager import Custommanager
    # Create your models here.

class CustomUser(AbstractUser):
    username = None 
    phone_number = models.CharField(unique=True,max_length=10)
    age = models.IntegerField(default=18)
    gender = models.CharField(choices = 
                              (('Male','Male'),
                                ('Female','Female')),max_length=100)
    profile_picture = models.ImageField(upload_to="profile/images/")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = Custommanager()
    #WHEN WE ARE CREATING CUSTOM USER DATA MODEL.., WE NEED TO CREATE MANAGER.PY