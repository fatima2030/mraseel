from django.urls import path
from notify.views import ShowNOtifications, DeleteNotification,accept

app_name = 'notify'

urlpatterns = [
   	path('', ShowNOtifications, name='show-notifications'),
   	path('<noti_id>/delete', DeleteNotification, name='delete-notification'),
   	path('<noti_id>/accept', accept, name='accept'),



	   
	


]