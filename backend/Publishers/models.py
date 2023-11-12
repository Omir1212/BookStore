from django.db import models



class Publisher(models.Model):

    def __str__(self):
        return self.name
    

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

