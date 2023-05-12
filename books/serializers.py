from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'author', 'isbn', 'price', 'status',
                  'description', 'language', 'text', 'pages', 'year_of_publication']
