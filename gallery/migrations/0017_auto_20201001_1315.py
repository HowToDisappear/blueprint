# Generated by Django 3.0.8 on 2020-10-01 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0016_delete_event'),
    ]

    operations = [
        migrations.RenameModel('Art', 'Artwork'),
    ]
