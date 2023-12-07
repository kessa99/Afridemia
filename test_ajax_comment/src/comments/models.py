from django.db import models

class Comment(models.Model):
    auteur = models.CharField(max_length=100, default='')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)