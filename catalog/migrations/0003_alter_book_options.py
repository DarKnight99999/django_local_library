# Generated by Django 4.1.2 on 2022-11-11 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['isbn']},
        ),
    ]
