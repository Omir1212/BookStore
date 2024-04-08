from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(
        to=User,
        null=False,
        unique=True,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(max_length=18, unique=True)  # nullable
    user_type = models.CharField(
        choices=[
            ("author", "author"),
            ("publisher", "publisher"),
            ("customer", "customer"),
        ],
        max_length=9,
        null=False,
    )
    selected_role = models.CharField(
        choices=[
            ("author", "author"),
            ("publisher", "publisher"),
            ("customer", "customer"),
        ],
        max_length=14,
        null=False,
    )

    class meta:
        db_table = 'app_user'


class Author(models.Model):
    app_user = models.OneToOneField(
        to=AppUser,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    bio = models.TextField(
        blank=False,
        null=False
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    genre = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.CASCADE,
        related_name='books'
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publication_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'book'


class Publisher(models.Model):
    app_user = models.OneToOneField(
        to=AppUser,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'publisher'
