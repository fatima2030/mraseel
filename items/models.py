from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
from notify.models import Notification

CITY = (
    
        ('الخرطوم', 'الخرطوم'),
        ('بحري', 'بحري'),
        ('امدرمان', 'امدرمان'),
    )


class Category(models.Model):
    COLORS = (
        ('S', 'success'),
        ('P', 'primary'),
        ('I', 'info'),
        ('W', 'warning'),
        ('D', 'danger'),
        ('A', 'dark'),
        ('E', 'secondary'),
        ('L', 'light')
    )

    ICONS = (
        ('T', 'mobile-alt'),
        ('B', 'book'),
        ('M', 'music'),
        ('C', 'car'),
        ('H', 'home'),
        ('A', 'basketball-ball'),
        ('E', 'headphones'),
        ('D', 'baby-carriage'), 
    )
    name = models.CharField(max_length=50)
    #color = models.CharField(max_length=1, choices=COLORS, default='P')
    #icon = models.CharField(max_length=12, choices=ICONS, default='B')

    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name    


class Item(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='items')

    name = models.CharField(max_length=50)
    From = models.CharField(max_length=350 , default='from'  )
    to = models.CharField(max_length=350 ,default='to')


    description = models.TextField(max_length=250 ,null=True)
    price = models.FloatField()
    is_available = models.BooleanField(default=True) 
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    city = models.CharField(max_length=25, choices=CITY ,default='1')

    slug = models.SlugField(unique=False, null=True, blank=True)
    num = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.num)
        return super(Item, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    
class ItemRental(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    hirer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    fulfilled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def user_rent_item(sender, instance, *args, **kwargs):
	    Rent = instance
	    recv = Rent.item
	    sender = Rent.hirer
	    notify = Notification( sender=sender, user=recv.owner  , notification_type=1)
	    notify.save()


    


post_save.connect(ItemRental.user_rent_item, sender=ItemRental)


