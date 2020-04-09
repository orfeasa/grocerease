from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.models import Category, Order, OrderItem, Product, User

admin.site.register(Product)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
