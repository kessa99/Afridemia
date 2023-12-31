from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poll_questions", null=True, blank=True)
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.option
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return self.user.username