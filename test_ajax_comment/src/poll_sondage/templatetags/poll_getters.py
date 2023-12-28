from django import template
from django.shortcuts import get_object_or_404
from poll_sondage.models import *

register = template.Library()


@register.filter
def get_choices(pk):
    poll = get_object_or_404(Question, id=pk)
    choices= Choice.objects.filter(question=poll)
    return choices

@register.filter
def get_choice_percentage(pk):
    choice = get_object_or_404(Choice, id=pk)
    vote= Vote.objects.filter(choice=choice)
    return vote

@register.filter
def get_total_vote(pk):
    poll = get_object_or_404(Question, id=pk)
    vote= Vote.objects.filter(question=poll)
    return vote

@register.filter
def calculate_percentage(choice, total_votes):
    if total_votes.count() == 0:
        return 0
    return (choice.count() / total_votes.count()) * 100