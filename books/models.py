from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    is_active = models.BooleanField()
    description = models.TextField()
    language = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    pages = models.IntegerField()
    year_of_publication = models.IntegerField()


    def __str__(self):
        return self.title

