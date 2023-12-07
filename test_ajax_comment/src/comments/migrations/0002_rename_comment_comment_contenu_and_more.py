# Generated by Django 4.2.7 on 2023-11-27 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='contenu',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='auteur',
            field=models.CharField(default='', max_length=100),
        ),
    ]
