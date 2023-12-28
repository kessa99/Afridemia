from django import forms
from .models import Comment_revu, Revue

class RevuForm(forms.ModelForm):
    class Meta:
        model = Revue
        fields = '__all__'
        exclude=('likes_revue', 'like_count_revu', 'download_count',)

class CommentRevuForm(forms.ModelForm):
    class Meta:
        model = Comment_revu
        fields = ['contenu']

    contenu = forms.CharField(
        widget=forms.Textarea(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
    )