# Generated by Django 4.2.7 on 2023-12-01 09:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Bourse', '0003_bourse_like_count_alter_bourse_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='bourse',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='bourse',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='bourse',
            name='fichier_a_joindre',
            field=models.FileField(default='', upload_to='bourse_files/'),
        ),
        migrations.AddField(
            model_name='bourse',
            name='lieu',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bourse',
            name='niveau',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.CreateModel(
            name='Postulant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('bourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bourse.bourse')),
            ],
        ),
    ]
