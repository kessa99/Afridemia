# Generated by Django 4.2.7 on 2023-11-29 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bourse', '0002_bourse_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bourse',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='likes',
            field=models.ManyToManyField(blank='True', default='None', related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
