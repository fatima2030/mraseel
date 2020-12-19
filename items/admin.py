from django.contrib import admin
from items.models import Item, Category, ItemRental

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ItemRental)
