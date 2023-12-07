# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def liste_commentaires(request):
    commentaires = Comment.objects.all()
    form = CommentForm()
    context = {'commentaires': commentaires, 'form': form}
    print(commentaires) 
    return render(request, 'comments/index.html', context)

@login_required
@require_POST
def ajouter_commentaire(request):
    form = CommentForm(request.POST)
    
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})
