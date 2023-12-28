from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Archive, CommentArchive
from .forms import ArchiveForm, ArchiveCommentForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def saisie_archive(request):
    if request.method == 'POST':
        form = ArchiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'archive/liste_archive.html', {})
    else:
        form = ArchiveForm()
    return render(request, 'archive/saisie_archive.html', {'form': form})


@login_required
def liste_archive(request):
    archive = Archive.objects.all()
    return render(request, 'archive/liste_archive.html', {'archive': archive})

@login_required
def liste_archive_admin(request):
    archive = Archive.objects.all()
    return render(request, 'archive/liste_archive_admin.html', {'archive': archive})




@login_required
@require_POST
def ajouter_commentaire_archive(request, archive_id):
    archive_instance = get_object_or_404(Archive, pk=archive_id)
    form = ArchiveCommentForm(request.POST)

    if form.is_valid():
        new_comment_archive = form.save(commit=False)
        new_comment_archive.archive = archive_instance
        new_comment_archive.save()
        return JsonResponse({'success': True, 'comment_archive_id': new_comment_archive.id})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})

@login_required
def liste_comment_archive(request, archive_id):
    archive_comments = CommentArchive.objects.filter(archive_id=archive_id)
    comments_archive = [{'auteur': comment.auteur, 'date': comment.date, 'contenu': comment.contenu} for comment in archive_comments]
    return JsonResponse({'comments': comments_archive})


@login_required
def detail_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    commentaire_archive = CommentArchive.objects.filter(archive=archive)
    new_comment_archive = None

    if request.method == 'POST':
        comment_archive_form = ArchiveCommentForm(data=request.POST)
        if comment_archive_form.is_valid():
            new_comment_archive = comment_archive_form.save(commit=False)
            new_comment_archive.archive = archive
            new_comment_archive.save()
    else:
        comment_archive_form = ArchiveCommentForm()
    context = {'archive': archive, 'commentaire_archive': commentaire_archive, 'comment_archive_form': comment_archive_form, 'new_comment_archive': new_comment_archive}
    return render(request, 'archive/detail_archive.html', context)





@login_required
def detail_archive_admin(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    return render(request, 'archive/detail_archive_admin.html', {'archive': archive})

@login_required
def modifie_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    if request.method =='POST':
        form = ArchiveForm(request.POST, instance=archive)
        if form.is_valid():
            form.save()
            return redirect('detail_archive_admin', archive_id=archive_id)
    else:
        form = ArchiveForm(instance=archive)
    context = {
        'form': form,
        'archive': archive,
    }
    return render(request, 'archive/modifie_archive.html', context)


@login_required
def supprime_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)
    if request.method == 'POST':
        archive.delete()
        return redirect('liste_archive')
    return render(request, 'archive/supprime_archive.html', {'archive': archive})


@login_required
@require_POST
def archive_like(request):
    if request.POST.get('action') == 'post':
        archive_id_str = request.POST.get('archiveId')

        if archive_id_str is not None and archive_id_str.isdigit():
            archive_id = int(archive_id_str)
            archive = get_object_or_404(Archive, id=archive_id)

            # Vérifiez si l'utilisateur a déjà aimé cette archive
            if archive.archive_likes.filter(id=request.user.id).exists():
                archive.archive_likes.remove(request.user)
                archive.archive_like_count -= 1
                result = archive.archive_like_count
            else:
                archive.archive_likes.add(request.user)
                archive.archive_like_count += 1
                result = archive.archive_like_count
            archive.save()
            return JsonResponse({'result': result})
    return JsonResponse({'result': 'error'})




@login_required
def telecharger_document_archive(request, archive_id):
    archive = get_object_or_404(Archive, pk=archive_id)

    if archive.fichier:
        # Incrémenter le compteur de téléchargements
        archive.download_count += 1
        archive.save()

        response = HttpResponse(archive.fichier, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{archive.fichier.name}"'
        return response
    else:
        return HttpResponse("Le fichier n'est pas disponible pour le téléchargement.")