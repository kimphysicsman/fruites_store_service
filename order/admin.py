from django.contrib import admin

from order.models import Order, PriceOrder

admin.site.register(Order)
admin.site.register(PriceOrder)