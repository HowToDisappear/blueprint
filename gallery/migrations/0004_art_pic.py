# Generated by Django 3.0.8 on 2020-08-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='pic',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
