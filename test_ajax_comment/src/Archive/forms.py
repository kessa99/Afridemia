from django import forms
from .models import *

class ArchiveForm(forms.ModelForm):
    class Meta:
        model = Archive
        fields = '__all__'
        exclude=('archive_likes', 'archive_like_count', 'download_count',) 

class ArchiveCommentForm(forms.ModelForm):
    class Meta:
        model = CommentArchive
        fields = ['contenu']
    
    contenu = forms.CharField(
        widget=forms.Textarea(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
    )