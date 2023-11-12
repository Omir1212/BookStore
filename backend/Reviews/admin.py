from django.contrib import admin
from .models import Review




class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['id']













admin.site.register(Review, ReviewAdmin)
