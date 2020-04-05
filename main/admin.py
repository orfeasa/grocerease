from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import User, Product, Category, Order, OrderItem

admin.site.register(Product)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
