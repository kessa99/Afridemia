from django import forms
from .models import Comment, Bourse, Postulant

class BourseForm(forms.ModelForm):
    class Meta:
        model = Bourse
        fields = '__all__'
        exclude=('likes', 'like_count',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contenu']

    contenu = forms.CharField(
        widget=forms.Textarea(attrs={'class': ' placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm items-center'}),
    )

class PostulerForm(forms.ModelForm):
    class Meta:
        model = Postulant
        fields = ['nom', 'email', 'contenu']