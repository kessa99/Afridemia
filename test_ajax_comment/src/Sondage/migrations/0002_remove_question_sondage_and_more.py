# Generated by Django 4.2.7 on 2023-12-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sondage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='sondage',
        ),
        migrations.RenameField(
            model_name='sondage',
            old_name='message',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='sondage',
            name='image',
        ),
        migrations.AddField(
            model_name='sondage',
            name='type_reponse',
            field=models.CharField(choices=[('RC', 'Réponse courte'), ('P', 'Paragraphe'), ('CC', 'Case à cocher'), ('MC', 'Multiple Choix'), ('LD', 'Liste déroulante'), ('IF', 'Importer un fichier'), ('GCM', 'Grille à Choix multiples'), ('GCC', 'Grille à cases à cocher'), ('D', 'Date'), ('H', 'Heure'), ('I', 'Image')], default='Reponse courte', max_length=50),
        ),
        migrations.DeleteModel(
            name='OptionReponse',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]