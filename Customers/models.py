from django.db import models




class Customer(models.Model):

    def __str__(self):
        return self.Username
    
    Username = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Password = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Email = models.EmailField(
        max_length=200,
        null=False,
        blank=False,
    )

    Address = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Phone_Number = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Customers'
