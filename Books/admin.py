from django.contrib import admin
from .models import Book




class BookAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Title',]













admin.site.register(Book , BookAdmin)
