from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Dans votre fichier Python
# from customUser.models import CustomUser

from django.urls import reverse

scholarship_types = (
    ('partial', 'Partielle'),
    ('full', "Complete"),
)

class Bourse(models.Model):
    titre  = models.CharField(max_length=255)
    publicateur = models.CharField(max_length=255)
    categorie  = models.CharField(max_length=255)
    financement = models.CharField(max_length=255)
    nature = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255, default='')
    niveau = models.CharField(max_length=50, default='')
    description = models.TextField(default='', blank=True, null=True)
    cover_photo = models.ImageField(blank=True, null=True, upload_to="images/")
    fichier_a_joindre = models.FileField(upload_to='bourse_files/', default='')
    likes = models.ManyToManyField(User, related_name='like', default="None", blank="True")
    like_count = models.BigIntegerField(default='0')

    def number_like(self):
        return self.likes.count()

class Comment(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100, default='')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Postulant(models.Model):
    bourse = models.ForeignKey(Bourse, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)