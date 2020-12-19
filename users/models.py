from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser



CARS = (
    
        ('ركشه', 'ركشه'),
        ('هايس', 'هايس'),
        ('موتر', 'موتر'),
        ('عربيه خاصه', 'عربيه خاصه'),
    )



class UserProfile(AbstractUser):

    bio = models.CharField(max_length=100,default='1')
    telephone = models.IntegerField( default='1' ,null=False) 
    car_type = models.CharField(choices=CARS ,max_length=20)
    your_picture = models.ImageField(default='static/images/logo.png', upload_to='images/' )     
    #number_picture = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/' )  

class working(models.Model):
    name = models.CharField(max_length=60 )
    bio = models.CharField(max_length=100,default='abc')
    telephone = models.IntegerField() 
    car_type = models.CharField(max_length=12,choices=CARS ,default='1')
    your_picture = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/')     
    number_picture = models.ImageField(default='profile_pictures/default.jpg', upload_to='profile_pictures/')     
