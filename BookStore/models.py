from django.db import models
from django.forms import ValidationError

# Create your models here.

class Book(models.Model):

    def __str__(self):
        return self.Title
    
    def validate_max_rating(value):
        if value > 5.0: 
            raise ValidationError("The maximum rating allowed is 5.0.")

    Title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    # Many-to-Many relationship with Author
    authors = models.ManyToManyField('Author', related_name='books')

    ISBN = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Price = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Publication_Date = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    # Many-to-Many relationship with Genre
    genres = models.ManyToManyField('Genre', related_name='books')

    # Many-to-Many relationship with Publisher
    publishers = models.ManyToManyField('Publisher', related_name='books')

    Language = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Average_Rating = models.FloatField(
        validators=[validate_max_rating],
        null=False,
        blank=False,
    )

    Quantity = models.IntegerField(
        null=False,
        blank=False,
    )

    Cover_Image = models.ImageField(
        null=True,
        blank=True,
    )

    Description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Books'

        


class Author(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Biography = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Authors'


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Description = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Genres'


class Publisher(models.Model):
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Address = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Contact_Info = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Publishers'


class Customer(models.Model):
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


class Order(models.Model):
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


class Review(models.Model):
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
