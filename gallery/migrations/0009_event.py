# Generated by Django 3.0.8 on 2020-09-30 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0008_auto_20200927_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('pricem', models.IntegerField(blank=True, null=True)),
                ('descr', models.CharField(blank=True, max_length=10000, null=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Artist')),
                ('artwork', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gallery.Art')),
                ('visitors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
