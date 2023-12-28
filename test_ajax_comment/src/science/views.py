from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db.models import F

# Create your views here.

@login_required
def saisir_revue(request):
    if request.method == 'POST':
        print("Formulaire soumis !")
        form = RevuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulaire valide !")
        return redirect('science:list_revue')
    else:
        form = RevuForm()
    context = {
        'form':form,
    }
    return render(request, 'science/saisir_revue.html', context)

@login_required
def list_revue(request):
    revue = Revue.objects.all()
    context = {'revue': revue}
    return render(request, 'science/list_revue.html', context)

@login_required
def list_revue_admin(request):
    revue = Revue.objects.all()
    context = {'revue': revue}
    return render(request, 'science/list_revue_admin.html', context)
    

@login_required
def modifie_revue(request, revue_id):
    revue = get_object_or_404(Revue, pk=revue_id)

    if request.method == 'POST':
        form = RevuForm(request.POST, instance=revue)
        if form.is_valid():
            form.save()
            return redirect('science:details_revue_admin', revue_id=revue_id)
    else:
        form = RevuForm(instance=revue)
    context = {
        'form': form,
        'revue': revue,
    }

    return render(request, 'science/modifie_revue.html', context)

def supprime_revue(request, revue_id):
    revue = get_object_or_404(Revue, pk=revue_id)
    if request.method == 'POST':
        revue.delete()
        return redirect('science:list_revue_admin')
    context = {'revue':revue}
    return render(request, 'science/supprime_revue.html', context)






@login_required
@require_POST
def ajouter_commentaire_revue(request, revue_id):
    revue = get_object_or_404(Revue, pk=revue_id)
    form = CommentRevuForm(request.POST)

    if form.is_valid():
        new_comment_revue = form.save(commit=False)
        new_comment_revue.revue = revue
        new_comment_revue.save()
        return JsonResponse({'success': True, 'comment_revue_id': new_comment_revue.id})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})

@login_required
def liste_commentaire_revue(request, revue_id):
    revue_comments = Comment_revu.objects.filter(revue_id=revue_id)
    comments_revue = [{'auteur': comment.auteur, 'date': comment.date, 'contenu': comment.contenu} for comment in revue_comments]
    return JsonResponse({'comments': comments_revue})

@login_required
def detail_revue(request, revue_id):
    revue = get_object_or_404(Revue, id=revue_id)
    commentaire_revue = Comment_revu.objects.filter(revue_id=revue_id)
    new_comment_revue = None

    if request.method == 'POST':
        comment_revue_form = CommentRevuForm(data=request.POST)
        if comment_revue_form.is_valid():
            new_comment_revue = comment_revue_form.save(commit=False)
            new_comment_revue.revue = revue
            new_comment_revue.save()
    else:
        comment_revue_form = CommentRevuForm()

    context = {
        'revue': revue,
        'commentaire_revue': commentaire_revue,
        'comment_revue_form': comment_revue_form,
        'new_comment_revue': new_comment_revue,
    }
    return render(request, 'science/detail_revue.html', context)

    
    
@login_required
def details_revue_admin(request, revue_id):
    revue = get_object_or_404(Revue, pk=revue_id)
    context = {'revue':revue}
    return render(request, 'science/details_revue_admin.html', context)

@login_required
@require_POST
def revue_like(request):
    if request.POST.get('action') == 'post':
        revue_id_str = request.POST.get('revueId')

        if revue_id_str is not None and revue_id_str.isdigit():
            revue_id = int(revue_id_str)
            revue = get_object_or_404(Revue, id=revue_id) 

            # Vérifiez si l'utilisateur a déjà aimé cette revue
            if revue.likes_revue.filter(id=request.user.id).exists():
                revue.likes_revue.remove(request.user)
                revue.like_count_revu -= 1
                result = revue.like_count_revu
            else:
                revue.likes_revue.add(request.user)
                revue.like_count_revu += 1
                result = revue.like_count_revu
            revue.save()
            return JsonResponse({'result': result})
    return JsonResponse({'result': 'error'})


@login_required
def telecharger_document_revue(request, revue_id):
    revue = get_object_or_404(Revue, pk=revue_id)

    if revue.file:
        # Incrémente le champ download_count
        Revue.objects.filter(id=revue.id).update(download_count=F('download_count') + 1)

        file_path = os.path.join(settings.MEDIA_ROOT, revue.file.name)
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
            return response
    else:
        return HttpResponse("Le fichier n'est pas disponible pour le téléchargement.")