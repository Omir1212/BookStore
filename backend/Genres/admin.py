from django.contrib import admin
from .models import Genre




class GenreAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']













admin.site.register(Genre, GenreAdmin)
