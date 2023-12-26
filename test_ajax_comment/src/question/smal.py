from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Question, Answer

@login_required
@require_POST
def vote(request):
    if request.POST.get('action') == 'post':
        question_uid = request.POST.get('question_uid')
        answer_uid = request.POST.get('answer_uid')

        # Vérifiez si la question et la réponse existent
        question = get_object_or_404(Question, uid=question_uid)
        answer = get_object_or_404(Answer, uid=answer_uid)

        # Vérifiez si l'utilisateur a déjà voté pour cette question
        if question.answers.filter(voters=request.user.uid).exists():
            question.answers.remove(request.user)
            question.counter -=1
            result = question.counter
        else:
            question.answers.add(request.user)
            question.counter +=1
            result = question.counter
        question.save()
        return JsonResponse({'result': 'success', 'message': 'Votre vote a été enregistré avec succès.'})

    return JsonResponse({'result': 'error', 'message': 'Mauvaise requête.'})
