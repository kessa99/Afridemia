from django.db import models
from .choices import CATEGORIE_CHOICES, TYPES_EVENT, BILLET
from timezone_field import TimeZoneField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    description = models.TextField(default='', blank=True, null=True)
    categorie = models.CharField(max_length=255, choices=CATEGORIE_CHOICES)
    organisateur = models.CharField(max_length=255, default='')
    type_event = models.CharField(max_length=255, choices=TYPES_EVENT)
    format_event = models.CharField(max_length=255, default='')
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    date_heure_debut = models.DateTimeField(null=True, blank=True)
    date_heure_fin = models.DateTimeField(null=True, blank=True)
    billet = models.CharField(max_length=50, choices=BILLET)
    fuseau_horaire = TimeZoneField(default='UTC')
    intervenant = models.CharField(max_length=255)
    event_likes = models.ManyToManyField(User, related_name='event_like', default="None", blank="True")
    event_like_count = models.BigIntegerField(default='0')

    def number_like(self):
        return self.event_likes.count()

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100, default='')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    contenu = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)