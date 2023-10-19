from django.db import models




class Genre(models.Model):

    def __str__(self):
        return self.name
    
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

