# Generated by Django 4.2.7 on 2023-12-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bourse', '0004_bourse_cover_photo_bourse_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bourse',
            name='financement',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='nature',
            field=models.CharField(max_length=255),
        ),
    ]
