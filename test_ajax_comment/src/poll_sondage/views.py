from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, Vote
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def create_poll_index(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        choices = request.POST.getlist('choices')

        # Vérifions si la question et au moins une réponse sont présentes
        if question_text and choices:
            question_obj = Question.objects.create(
                user=request.user,
                question=question_text,
            )

            # Supposons que les réponses sont séparées par des lignes dans le champ de formulaire
            for choice in choices:
                Choice.objects.create(option=choice, question=question_obj)

            messages.success(request, 'Sondage créé avec succès.')
            return redirect('my_question:liste_sondage_admin_index')
        else:
            messages.error(request, 'Veuillez saisir au moins une réponse.')

    return render(request, 'poll_sondage/create_poll.html')



@login_required
def liste_sondage_admin_index(request):
    questions = Question.objects.all()
    return render(request ,'poll_sondage/liste_sondage_admin.html', {'questions' : questions})

@login_required
def details_poll(request, pk):
    poll = get_object_or_404(Question, id=pk)
    votes = Vote.objects.filter(question=poll)
    context = {'poll':poll, 'votes':votes}
    return render(request, 'poll_sondage/details_poll.html', context)

# @login_required
# def vote(request, sond_id):
#     question = get_object_or_404(Question, id=sond_id)
#     options = question.choices.all()

#     if request.method == 'POST':
#         selected_option_id = request.POST.get('choice')

#         if selected_option_id:
#             selected_option = options.get(id=selected_option_id)
#             selected_option.vote += 1
#             selected_option.save()

#             messages.success(request, 'Votre vote a été enregistré avec succès.')
#             return redirect('my_question:result', sond_id)  # Rediriger vers la page de résultats

#         else:
#             messages.error(request, 'Veuillez sélectionner une option avant de voter.')

#     return render(request, 'poll_sondage/question.html', {'question_result': question, 'option_result': options})

@login_required
def add_vote(request, id):
    user = request.user
    question = get_object_or_404(Question, id=id)
    options = question.choices.all()

    if request.method == 'POST':
        selected_option_id = request.POST.get('choice')
        selected_choice = get_object_or_404(Choice, id=selected_option_id)
        new_vote = Vote.objects.create(
            user=user,
            question=question,
            choice=selected_choice,
        )
        new_vote.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))