# Generated by Django 3.2.8 on 2021-10-16 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]