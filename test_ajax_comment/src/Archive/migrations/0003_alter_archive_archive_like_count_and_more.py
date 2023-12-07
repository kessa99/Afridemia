# Generated by Django 4.2.7 on 2023-12-04 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Archive', '0002_alter_archive_archive_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='archive_like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='archive_likes',
            field=models.ManyToManyField(blank='True', default='None', related_name='archive_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
