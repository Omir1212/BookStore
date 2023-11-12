from django.contrib import admin
from .models import Order




class OrderAdmin(admin.ModelAdmin):
    search_fields = ['id']













admin.site.register(Order, OrderAdmin)