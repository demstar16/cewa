# Generated by Django 4.2.2 on 2023-06-13 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cewa_app', '0003_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
