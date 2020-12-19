from django import forms

from items.models import Category, Item 



class ItemCreateForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'From','to','price','city','description', 'price',]  

        widgets = {
            'description': forms.TextInput(attrs={'placeholder':  ' تفاصيل الطلب "اختياري" ',} )
        
        }
        labels ={'name':'طلبك شنو','From':'مكان الطلب بالتفصيل','to':'مكان التوصيل بالتفصيل','price':'سعر التوصيل' ,'description':'تفاصيل','city':'المدينه',}
    def __init__(self, *args,**kwargs):
        super(ItemCreateForm ,self).__init__(*args,**kwargs)
        self.fields['description'].required = False
        