from django.contrib import admin

from product.models import (
    Product, 
    Price
)

admin.site.register(Price)
admin.site.register(Product)