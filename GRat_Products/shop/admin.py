from django.contrib import admin
from .models import Product, Order, OrderItem, ShippingAddress
from django.contrib.auth.models import User


class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

