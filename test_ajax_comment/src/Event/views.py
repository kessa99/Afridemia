from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def saisir_event(request):
    if request.method == 'POST':
        print("Formulaire soumis !")
        form = EventForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            print("Formulaire valide !")
            return redirect('event:list_event')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'event/saisir_event.html', context)

@login_required
def modifie_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method =='POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event:details_Event_admin', event_id=event_id)
    else:
        form = EventForm(instance=event)
    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'event/modifie_event.html', context)

@login_required
def supprime_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('liste_event')
    return render(request, 'event/supprime_event.html', {'event': event})


@login_required
def list_event(request):
    event = Event.objects.all()
    contexte = {'event':event}
    return render(request, 'event/liste_event.html', contexte)

@login_required
def list_event_admin(request):
    event = Event.objects.all()
    context = {'event': event}
    return render(request, 'event/list_event_admin.html', context)

@login_required
@require_POST
def ajouter_commentaire_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    form = CommentEventForm(request.POST)

    if form.is_valid():
        new_comment_event = form.save(commit=False)
        new_comment_event.event = event
        new_comment_event.save()
        return JsonResponse({'success': True, 'comment_event_id': new_comment_event.id})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})


@login_required
def liste_commentaires(request, event_id):
    event_comments = Comment.objects.filter(event_id=event_id)
    comments_event = [{'auteur': comment.auteur, 'date': comment.date, 'contenu': comment.contenu} for comment in event_comments]
    return JsonResponse({'comments': comments_event})


def detail_Event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    commentaire_event = Comment.objects.filter(event=event)
    new_comment_event = None

    if request.method == 'POST':
        comment_event_form = CommentEventForm(data=request.POST)
        if comment_event_form.is_valid():
            new_comment_event = comment_event_form.save(commit=False)
            new_comment_event.event = event
            new_comment_event.save()
    else:
        comment_event_form = CommentEventForm()
    context = {'event': event, 'commentaire_event': commentaire_event, 'comment_event_form': comment_event_form, 'new_comment_event': new_comment_event}
    return render(request, 'event/detail_event.html', context)

@login_required
def details_event_admin(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participant = Participant.objects.filter(event=event)
    commentaire = Comment.objects.filter(event=event)
    return render(request, 'event/details_event_admin.html', {'event': event, 'participant': participant, 'commentaire':commentaire})

@login_required
def saisir_participant(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.event = event
            participant.save()
            return redirect('', event_id=event_id)
    else:
        form = ParticipantForm()
    context = {'form': form, 'participant':participant, 'form':form}
    return render(request, 'event/saisir_participant.html', context)

@login_required
def list_participant(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    participant = Participant.objects.filter(event_id=event_id)
    context = {'event': event, 'participant': participant}
    return render(request, 'event/liste_participant.html', context)


@login_required
@require_POST
def event_like(request):
    if request.POST.get('action') == 'post':
        event_id_str = request.POST.get('eventId')

        if event_id_str is not None and event_id_str.isdigit():
            event_id = int(event_id_str)
            event = get_object_or_404(Event, id=event_id)

            # Vérifiez si l'utilisateur a déjà aimé cette Event
            if event.event_likes.filter(id=request.user.id).exists():
                event.event_likes.remove(request.user)
                event.event_like_count -= 1
                result = event.event_like_count
            else:
                event.event_likes.add(request.user)
                event.event_like_count += 1
                result = event.event_like_count
            event.save()
            return JsonResponse({'result': result})
    return JsonResponse({'result': 'error'})