# Generated by Django 3.2.8 on 2021-10-16 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_update_or_create_books', 'Can update or create books'),)},
        ),
    ]