from django.db import models
import utilities as utils




class Book(models.Model):

    def __str__(self):
        return self.Title


    Title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )


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

    genres = models.ManyToManyField('Genres.Genre', related_name='books')


    publishers = models.ManyToManyField('Publishers.Publisher', related_name='books')

    Language = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    Average_Rating = models.FloatField(
        validators=[utils.validate_max_rating],
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

        


