from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .choices import EXAM_CHOICES, AFRICAN_COUNTRIES, SUBJECT_CHOICES

# Create your models here.

class Archive(models.Model):
    titre = models.CharField(max_length=255)
    publicateur = models.CharField(max_length=255)
    ecole = models.CharField(max_length=255)
    matiere = models.CharField(max_length=255, choices=SUBJECT_CHOICES)
    examen = models.CharField(max_length=255)
    pays = models.CharField(max_length=255, choices=AFRICAN_COUNTRIES)
    fichier = models.FileField(upload_to='archive_files/')
    niveau = models.CharField(max_length=4, choices=EXAM_CHOICES)
    archive_likes = models.ManyToManyField(User, related_name='archive_like', default="None", blank="True")
    archive_like_count = models.BigIntegerField(default='0')
    
    def number_like(self):
        return self.archive_likes.count()

class CommentArchive(models.Model):
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100, default='')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)