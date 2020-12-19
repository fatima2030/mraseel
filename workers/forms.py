from django import forms
from .models import working
from users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm





CARS = (
    
        ('ركشه', 'ركشه'),
        ('هايس', 'هايس'),
        ('موتر', 'موتر'),
        ('عربيه خاصه', 'عربيه خاصه'),
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True , label='اسم المستخدم'  )
    bio = forms.CharField(max_length=100, label='تعريف بسيط عنك',required=True)
    telephone = forms.IntegerField( label='رقم تلفونك',required=True) 
    car_type = forms.ChoiceField(choices=CARS , label='سايق شنو',required=True)
    your_picture = forms.ImageField( label='صوره ليك',required=True)     



    class Meta:
        model = UserProfile
        fields = ('username', 'password1', 'password2','telephone','bio','car_type','your_picture',)
      
    
class WorkerLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, label='تذكرني')
    username = forms.CharField( required=True , label='اسم المستخدم'  )
    password1 = forms.PasswordInput()


