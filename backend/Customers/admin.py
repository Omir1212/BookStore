from django.contrib import admin
from .models import Customer




class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Username']













admin.site.register(Customer, CustomerAdmin)
