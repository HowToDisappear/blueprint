# Generated by Django 3.0.8 on 2020-10-27 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourart', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-time']},
        ),
    ]
