from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from items.models import Item, ItemRental
from django.utils.translation import gettext_noop

from notify.models import Notification
# Create your views here.

def ShowNOtifications(request):
	user = request.user
	notifications = Notification.objects.filter(user=user).order_by('-date')
	Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
	
	template = loader.get_template('notify/notifications.html')

	context = {
		'notifications': notifications,
	}

	return HttpResponse(template.render(context, request))


def DeleteNotification(request, noti_id):
    user = request.user
    item = Notification.objects.filter(id=noti_id, user=user).delete()
    itm = Item.objects.filter(id=noti_id, owner=user).update(is_available=False)
    itm.is_available = False
     	
    return redirect('notify:show-notifications')

def accept(self, noti_id):
    user = self.user
    rental = Item.objects.get(owner=user)
    rental.is_available = False
    rental.save(update_fields=["is_available"])
   
    rental.save()
     	
    return redirect('notify:show-notifications')









def CountNotifications(request):
	count_notifications = 0
	if request.user.is_authenticated:
		count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()

	return {'count_notifications':count_notifications}

