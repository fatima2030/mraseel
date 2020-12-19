from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 
from django.db.models import Max
from users.models import UserProfile




class UserComments(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                              related_name='comments_by_me', verbose_name=_("Owner"))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', blank=True, null=True,
                               verbose_name=_("Parent"))
    comment = models.TextField(max_length=140, verbose_name=_("Comment"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("Updated"))
    image = models.ImageField(blank=True, null=True, verbose_name=_("Image"))


def determine_message_file(instance, filename):
    low = min([instance.sender.id, instance.receiver.id])
    high = max([instance.sender.id, instance.receiver.id])
    return f"messages/{low}_{high}/{filename}"





class Messages(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 related_name='user', verbose_name=_("user"))
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                               related_name='from_user', verbose_name=_("Sender"))
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                 related_name='to_user', verbose_name=_("Receiver"))
    message = models.TextField(max_length=140, verbose_name=_("Message"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    seen = models.DateTimeField(blank=True, null=True, verbose_name=_("Seen"))
    file = models.ImageField(blank=True, null=True,  upload_to='user_message_files/', verbose_name=_("File"))
    is_read = models.BooleanField(default=False)
    num = models.IntegerField(default=0)

    def send_message(from_user, to_user, message):
        sender_message = Messages(
			user=from_user,
			sender=from_user,
			receiver=to_user,
			message=message,
			is_read=True)
        sender_message.save()

        recipient_message = Messages(
            user=to_user,
            sender=from_user,
            message=message,
            receiver=from_user,)
        recipient_message.save()
        return sender_message
    def get_messages(receiver):
            messages = Messages.objects.filter(receiver=receiver).values('sender').annotate(last=Max('created')).order_by('-last')
            users = []
            for message in messages:
                users.append({
                    'user': UserProfile.objects.get(pk=message['sender']),
                    'last': message['last'],
                    'unread': Messages.objects.filter(receiver=receiver, receiver__pk=message['sender'], is_read=False).count()
                    })
            return users