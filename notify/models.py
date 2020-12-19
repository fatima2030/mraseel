from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Notification(models.Model):
	NOTIFICATION_TYPES = ((1,'new rent'),(2,'accept'), (3,'reves'))

	items = models.ForeignKey('items.Item', on_delete=models.CASCADE, related_name="noti_post", blank=True, null=True)
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="noti_from_user")
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="noti_to_user")
	notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
	text_preview = models.CharField(max_length=90, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)