from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from .models import Comment, Bourse, Postulant
from .forms import CommentForm, BourseForm, PostulerForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


@login_required
def saisie_bourse(request):
    if request.method == 'POST':
        form = BourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'bourse/liste_bourse.html', {})
    else:
        form = BourseForm()
    return render(request, 'bourse/saisir_bourse.html', {'form': form})


@login_required
def modifie_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if request.method =='POST':
        form = BourseForm(request.POST, instance=bourse)
        if form.is_valid():
            form.save()
            return redirect('bourse:details_bourse_admin', bourse_id=bourse_id)
    else:
        form = BourseForm(instance=bourse)
    context = {
        'form': form,
        'bourse': bourse,
    }
    return render(request, 'bourse/modifie_bourse.html', context)


@login_required
def supprime_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if request.method == 'POST':
        bourse.delete()
        return redirect('liste_bourse')
    return render(request, 'bourse/supprime_bourse.html', {'bourse': bourse})


@login_required
def liste_bourse(request):
    bourses = Bourse.objects.all()
    context = {'bourses': bourses}
    return render(request, 'bourse/liste_bourse.html', context)


@login_required
def liste_bourse_admin(request):
    bourse = Bourse.objects.all()
    return render(request, 'bourse/liste_bourse_admin.html', {'bourse': bourse})




@login_required
@require_POST
def ajouter_commentaire(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.bourse = bourse
        new_comment.save()
        return JsonResponse({'success': True, 'comment_id': new_comment.id})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})


@login_required  
def liste_commentaires(request, bourse_id):
    bourse_comments = Comment.objects.filter(bourse_id=bourse_id)
    comments = [{'auteur': comment.auteur, 'date': comment.date, 'contenu': comment.contenu} for comment in bourse_comments]
    return JsonResponse({'comments': comments})

@login_required
def detail_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, id=bourse_id)
    commentaire = Comment.objects.filter(bourse=bourse)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.bourse = bourse
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'bourse': bourse, 'commentaire': commentaire, 'comment_form': comment_form, 'new_comment': new_comment}
    return render(request, 'bourse/detail_bourse.html', context)


@login_required
def details_bourse_admin(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    postulants = Postulant.objects.filter(bourse=bourse)
    commentaire = Comment.objects.filter(bourse=bourse)
    return render(request, 'bourse/details_bourse_admin.html', {'bourse': bourse, 'postulants': postulants, 'commentaire':commentaire})


@login_required
def saisir_postulant(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)

    if request.method == 'POST':
        form = PostulerForm(request.POST)
        if form.is_valid():
            postulant = form.save(commit=False)
            postulant.bourse = bourse
            postulant.save()
            return redirect('bourse:detail_bourse', bourse_id=bourse_id)
    else:
        form = PostulerForm()
    context = {
        'form': form,
        'bourse': bourse,
    }
    return render(request, 'bourse/saisir_postulant.html', context)


@login_required
def liste_postulant(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    postulant = Postulant.objects.filter(bourse_id=bourse_id)
    return render(request, 'bourse/liste_postulant.html', {'postulant': postulant, 'bourse': bourse})


@login_required
def telecharger_document_bourse(request, bourse_id):
    bourse = get_object_or_404(Bourse, pk=bourse_id)
    if bourse.fichier_a_joindre:
        response = HttpResponse(bourse.fichier_a_joindre, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{bourse.fichier_a_joindre.name}"'
        return response
    else:
        return HttpResponse("Le fichier n'est pas disponible pour le téléchargement.")



@login_required
@require_POST
def like(request):
    if request.POST.get('action') == 'post':
        bourse_id_str = request.POST.get('bourseId')

        if bourse_id_str is not None and bourse_id_str.isdigit():
            bourse_id = int(bourse_id_str)
            bourse = get_object_or_404(Bourse, id=bourse_id)

            # Vérifiez si l'utilisateur a déjà aimé cette bourse
            if bourse.likes.filter(id=request.user.id).exists():
                bourse.likes.remove(request.user)
                bourse.like_count -= 1
                result = bourse.like_count
            else:
                bourse.likes.add(request.user)
                bourse.like_count += 1
                result = bourse.like_count
            bourse.save()
            return JsonResponse({'result': result})
    return JsonResponse({'result': 'error'})