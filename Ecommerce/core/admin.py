from django.contrib import admin

# Register your models here.

from .models import Item, OrderItem


admin.site.register(Item)
admin.site.register(OrderItem)