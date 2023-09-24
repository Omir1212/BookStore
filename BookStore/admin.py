from django.contrib import admin
from .models import Book, Author, Genre, Review, Order, Customer, Publisher

class BookStoreItemsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookStoreItemsAdmin)
admin.site.register(Author, BookStoreItemsAdmin)
admin.site.register(Genre, BookStoreItemsAdmin)
admin.site.register(Review, BookStoreItemsAdmin)
admin.site.register(Order, BookStoreItemsAdmin)
admin.site.register(Customer, BookStoreItemsAdmin)
admin.site.register(Publisher, BookStoreItemsAdmin)


