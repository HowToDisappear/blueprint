# Generated by Django 3.0.8 on 2020-09-30 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='descr',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
