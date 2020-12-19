from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,UserChangeForm,ReadOnlyPasswordHashField,ReadOnlyPasswordHashWidget
from django.contrib.auth.models import User
from .models import UserProfile,working
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)


CARS = (
    
        ('ركشه', 'ركشه'),
        ('هايس', 'هايس'),
        ('موتر', 'موتر'),
        ('عربيه خاصه', 'عربيه خاصه'),
    )

class RealDateInput(forms.DateInput):
    input_type = "date"


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True , label='اسم المستخدم'  )

    class Meta(UserCreationForm):
        model = UserProfile
        fields = UserCreationForm.Meta.fields +  (
        "password1","password2", "email","telephone")
       

        labels={ 
            'username':'اسم المستخدم' ,
            'password1':'الباسويرد' ,

            'password2' : 'عيد ادخال الباسويرد' ,

            'email' : 'ايميلك' ,
            'telephone' : 'رقم تلفونك' ,



            }
       
    
class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label='تذكرني')
    username = forms.CharField( required=True , label='اسم المستخدم'  )
    password1 = forms.PasswordInput()



class ProfileUpdateForm(UserChangeForm,ReadOnlyPasswordHashField,ReadOnlyPasswordHashWidget):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(""), 
    )     
    template_name = 'user/profile_edit.html'

  
    class Meta(UserChangeForm):
        model = UserProfile
        fields = [
             'email', 'telephone',]



class UserWorkerForm(forms.ModelForm):

     
    class Meta:
        model = working
        fields = ['name','telephone','bio','car_type','your_picture',]
        labels ={
            'name':'اسمك الثلاثي',
            'telephone':'رقم تلفونك',
            'bio':'تعريف بسيط عنك',
            'car_type':'سايق شنو' ,
            'your_picture':'صوره ليك',
            }



       

        



