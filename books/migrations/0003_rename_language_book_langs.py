# Generated by Django 4.2.1 on 2023-05-08 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_description_book_language_book_pages_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='language',
            new_name='langs',
        ),
    ]