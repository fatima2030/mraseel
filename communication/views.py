from django.db.models import Q
from django.urls import reverse,reverse_lazy
from django.utils import timezone

from communication.forms import MessageForm
from communication.models import Messages
from django.views.generic import ListView, DetailView, RedirectView, FormView
from django.contrib.auth.decorators import login_required
from django.template import loader, RequestContext
from django.http import HttpResponse
from users.models import UserProfile
from items.models import Item




from django.contrib.auth import get_user_model
User = get_user_model()





@login_required
def Inbox(request):
	messages = Messages.get_messages(receiver=request.user)
	active_direct = None
	directs = None

	if messages:
		message = messages[0]
		active_direct = message['user'].username
		directs = Messages.objects.filter(sender=request.user,receiver=message['user'])
		directs.update(is_read=True)
		for message in messages:
			if message['user'].username == active_direct:
				message['unread'] = 0

	context = {
		'directs': directs,
		'messages': messages,
		'active_direct': active_direct,
		}

	template = loader.get_template('communication/direct.html')

	return HttpResponse(template.render(context, request))


@login_required
def Directs(request, username):
	user = request.user
	messages = Messages.get_messages(receiver=user)
	active_direct = username
	directs = Messages.objects.filter(receiver__username=username,user=user)
	directs.update(is_read=True)
	for message in messages:
		if message['user'].username == username:
			message['unread'] = 0

	context = {'directs': directs,'messages': messages,'active_direct':active_direct,}

	template = loader.get_template('communication/direct.html')

	return HttpResponse(template.render(context, request))



class MessagesListView(ListView):
    model = Messages
    context_object_name = 'message_list' 
    template_name = "communication/messages_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        
        context = super().get_context_data(object_list=object_list, **kwargs) 
        qs =  Messages.objects.filter(receiver=self.request.user,is_read=False).order_by('-created').values_list("sender",flat=True).distinct().annotate()
        o = UserProfile.objects.filter(pk__in=qs)  
        context = {'senders': o}
        return context


class MessagesListViewWoker(ListView):
    model = Messages
    context_object_name = 'message_list' 
    template_name = "communication/messages_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        
        context = super().get_context_data(object_list=object_list, **kwargs)
        qs =  Messages.objects.filter(receiver=self.request.user).order_by('-created').values_list("sender",flat=True).distinct().annotate()
        o = UserProfile.objects.filter(pk__in=qs)  
        context = {'senders': o}
        return context
         
         
class MessagesDetailView(ListView): 
    model = Messages
    template_name = "communication/messages_detail.html"
    def get_queryset(self):
        super().get_queryset().filter(
            Q(sender_id=self.kwargs["user_id"], receiver=self.request.user) & Q(seen__isnull=True)
        ).update(seen=timezone.now(),is_read=True)
        query =super().get_queryset().filter(
            Q(sender_id=self.kwargs["user_id"], receiver=self.request.user) |
            Q(receiver_id=self.kwargs["user_id"], sender=self.request.user)
        ).order_by("created")
        total = query.count()
        limit = 50
        offset = total - limit if total - limit > 0 else 0
        return query[offset:]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["other_user"] = UserProfile.objects.get(id=self.kwargs["user_id"])
        context["form"] = MessageForm()
        return context


class MessagesSendView(FormView):
    form_class = MessageForm
    template_name="communication/send_message.html"
    
    def get_success_url(self):
        return reverse_lazy("communication:messages_detail", kwargs={"user_id": self.kwargs["user_id"]})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_id"] = self.kwargs["user_id"]
        return context
    
    def form_valid(self, form):
        Messages.objects.create(
            user=self.request.user,

            sender=self.request.user,
            receiver_id=self.kwargs["user_id"],
            message=form.cleaned_data["message"],
            file=form.cleaned_data["file"]
        )
        return super().form_valid(form)



@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	message = request.POST.get('message')
	
	if request.method == 'POST':
		to_user = UserProfile.objects.get(username=to_user_username)
		Messages.send_message(from_user, to_user, message)
		return redirect('inbox')
	else:
		HttpResponseBadRequest()



@login_required
def SendDirect(request):
	from_user = request.user
	to_user_username = request.POST.get('to_user')
	message = request.POST.get('message')
	
	if request.method == 'POST':
		to_user = User.objects.get(username=to_user_username)
		Message.send_message(from_user, to_user, body)
		return redirect('communication:inbox')
	else:
		HttpResponseBadRequest()

def checkDirects(request):
    user = request.user
    directs_count = 0
    if request.user.is_authenticated:
        directs_count = Messages.objects.filter(receiver=user, is_read=False).count()

    return {'directs_count':directs_count}


class Accpt(ListView):
    model = Item
    template_name = 'communication/messages_detail.html'  
    context_object_name = 'accpet'


