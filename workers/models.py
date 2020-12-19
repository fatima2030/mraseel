from django.db import models
from django.conf import settings

from django.contrib.auth.models import User,AbstractUser,AbstractBaseUser


# Create your models here.


CARS = (
    
        ('ركشه', 'ركشه'),
        ('هايس', 'هايس'),
        ('موتر', 'موتر'),
        ('عربيه خاصه', 'عربيه خاصه'),
    )

class working(AbstractBaseUser):
    username = models.CharField(max_length=60 , unique=True,default='l')
    #name 				= models.CharField(max_length=60, unique=False) 
    bio = models.CharField(max_length=100,default='')
    telephone = models.IntegerField() 
    car_type = models.CharField(max_length=12,choices=CARS ,default='1')
    your_picture = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/')     
    number_picture = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/')  

    
    USERNAME_FIELD = 'username'
	
    def __str__(self):
        return self.username
   
