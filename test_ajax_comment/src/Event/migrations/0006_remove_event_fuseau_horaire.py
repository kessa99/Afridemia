# Generated by Django 4.2.7 on 2023-12-27 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0005_alter_event_billet_alter_event_categorie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='fuseau_horaire',
        ),
    ]