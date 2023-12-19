from django.forms import ModelForm
from .models import Sondagechoix
from django import forms

class CreatePollForm(ModelForm):
    class Meta:
        model = Sondagechoix
        fields = ['question', 'option_one', 'option_two', 'option_three']
