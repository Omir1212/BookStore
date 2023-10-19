from django.contrib import admin
from .models import Customer




class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Title',]













admin.site.register(Customer, CustomerAdmin)
