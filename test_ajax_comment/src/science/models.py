from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Revue(models.Model):
    titre = models.CharField(max_length=300)
    summary = models.TextField()
    authors = models.CharField(max_length=500, default='')
    introduction = models.TextField()
    methodology  = models.TextField()
    result  = models.TextField()
    Conclusion  = models.TextField()
    bibliography  = models.TextField()
    thanks  = models.TextField()
    conflict  = models.TextField()
    declarations  = models.TextField()
    file = models.FileField(upload_to='revue_files/', default='')
    likes_revue = models.ManyToManyField(User, related_name='like_revu', default='None', blank='True')
    like_count_revu = models.BigIntegerField(default='0')
    
    def number_like_revu(self):
        return self.likes_revue.count()

class Comment_revu(models.Model):
    revue = models.ForeignKey(Revue, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=100, default='')
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

