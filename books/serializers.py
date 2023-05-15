from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'author', 'isbn', 'price', 'is_active',
                  'description', 'language', 'text', 'pages', 'year_of_publication']

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # this code will check if it contains only alphabetical characters
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Book\'s title should be written with words'
                }
            )

        # Check author and title from DB existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'you can\'t upload if books\' title and authors are similar'
                }
            )


        return data
