from django.urls import path
from .views import MessagesListView, MessagesDetailView, MessagesSendView,Inbox,Directs,SendDirect,MessagesListViewWoker
app_name = 'communication'

urlpatterns = [
    path('', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='directs'),

    path('list/', MessagesListView.as_view(), name='messages_list'),
    path('detail/<int:user_id>/', MessagesDetailView.as_view(), name='messages_detail'),
    path('detail/<int:user_id>/send', MessagesSendView.as_view(), name='messages_send'),
    path('send/', SendDirect, name='send_direct'),
    path('show/', MessagesListViewWoker.as_view(), name='messages_show'),


]
 