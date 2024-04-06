from django.contrib import admin
from .models import Customer, Author, User


class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]


class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
    ]


admin.site.register(Customer, admin_class=CustomerAdmin)
admin.site.register(Author, admin_class=AuthorAdmin)
admin.site.register(User, admin_class=UserAdmin)
