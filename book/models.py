from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False
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
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        null=False
    )
    phone_number = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'publisher'