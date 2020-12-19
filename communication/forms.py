from django import forms
from django.utils.translation import gettext_lazy as _


class MessageForm(forms.Form):
    message = forms.CharField(max_length=140, label=_(" رساله"))
    file = forms.FileField(required=False, label=_("صوره"))

    widgets = {
        
        }