from django.contrib import admin
from .models import Publisher




class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']













admin.site.register(Publisher, PublisherAdmin)
