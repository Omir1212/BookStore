from django.db import models

from Books.models import Book
from Customers.models import Customer



class Review(models.Model):

    #def __str__(self):
        #return self.Rev
    
    Book = models.ForeignKey(Book, null= False, blank= False, on_delete=models.CASCADE)

    # Foreign Key relationship with Customer
    Customer = models.ForeignKey(Customer, null= False, blank= False, on_delete=models.CASCADE)

    Rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=False,
        blank=False,
    )

    ReviewText = models.TextField(
        max_length=200,
        null=False,
        blank=False,
    )

    Date_Posted = models.DateTimeField(
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Reviews'
