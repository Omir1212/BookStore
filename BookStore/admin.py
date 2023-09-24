from django.contrib import admin
from .models import Book, Author, Genre, Review, Order, Customer, Publisher

class BookAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Title',]

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', ]

class GenreAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', ]

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', ]

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Username', ]

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Customer__Username']

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Book__Title', ]




admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)




