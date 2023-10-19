from django.db import models

from django.core.validators import ValidationError




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
    authors = models.ManyToManyField('Authors.Author', related_name='books')

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
    genres = models.ManyToManyField('Genres.Genre', related_name='books')

    # Many-to-Many relationship with Publisher
    publishers = models.ManyToManyField('Publishers.Publisher', related_name='books')

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


    Description = models.TextField(
        max_length=200,
        null=False,
        blank=False,
    )

    class Meta:
        db_table = 'Books'

        


