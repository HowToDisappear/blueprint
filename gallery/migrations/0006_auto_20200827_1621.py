# Generated by Django 3.0.8 on 2020-08-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200827_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='descr',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.CharField(max_length=10000),
        ),
    ]
