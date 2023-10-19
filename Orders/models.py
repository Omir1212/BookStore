from django.db import models

#import all the needed 
from Customers.models import Customer



class Order(models.Model):

    # def __str__(self):
    #     return self.Customer
    
    # Foreign Key relationship with Customer
    Customer = models.ForeignKey(Customer, null= False, blank=False, on_delete=models.CASCADE, related_name='orders')

    OrderDate = models.DateTimeField(
        null=False,
        blank=False,
    )

    TotalPrice = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )

    Status = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    OrderItems = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Orders'


