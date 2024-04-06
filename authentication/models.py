from django.contrib.auth.models import AbstractUser, User
from django.db import models


class User(AbstractUser):
    class Meta:
        app_label = 'authentication'

    # Provide custom related_name for groups and user_permissions
    User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
    User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add customer-specific fields here


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add author-specific fields here
