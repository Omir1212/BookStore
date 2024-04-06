from django.contrib import admin

from .models import Book, Author, Publisher


class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "genre",
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "bio",
    ]


class PublisherAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "email",
        "phone_number",
        "address",
    ]


admin.site.register(Book, admin_class=BookAdmin)
admin.site.register(Author, admin_class=AuthorAdmin)
admin.site.register(Publisher, admin_class=PublisherAdmin)
